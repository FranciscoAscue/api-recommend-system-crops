from flask import Flask, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from flask_httpauth import HTTPTokenAuth
import mysql.connector
from datetime import datetime, timedelta
import os

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

VALID_TOKEN = "PgVPDqHJ9ffJ2Lx73bXvv9uraib1Y0eCYb9HvCa3aOluuzfkoMFJ1"

tokens = {
    VALID_TOKEN: "user"
}

last_update_file = 'last_update.txt'

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    return None
def save_last_update():
    with open(last_update_file, 'w') as file:
        file.write(datetime.now().isoformat())


def load_data_from_mysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123a456",
        database="foreslab_catalogue"
    )

    query = "SELECT * FROM `recommendations`"
    cursor = mydb.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['id', 'Family', 'valor', 'Country','time1','time2'])
    df_reestructurado = pd.pivot_table(df, values='valor', index='Family', columns='Country', aggfunc='first')
    cursor.close()
    mydb.close()

    csv_path = 'reconstructed_df.csv'
    df_reestructurado.to_csv(csv_path, index=True)
    save_last_update()

    return df_reestructurado

def load_last_update():
    if os.path.exists(last_update_file):
        with open(last_update_file, 'r') as file:
            last_update_str = file.read().strip()
            return datetime.fromisoformat(last_update_str)
    return None

def should_update_data():
    last_update = load_last_update()
    if last_update is None:
        return True  # Si nunca se ha actualizado, se debe actualizar ahora
    return (datetime.now() - last_update) >= timedelta(days=7)

def get_recommendations(column_name, reconstructed_df, top_n=5):
    column_idx = reconstructed_df.columns.get_loc(column_name)
    item_similarity = cosine_similarity(reconstructed_df.T)
    column_similarities = item_similarity[column_idx]
    similar_indices = column_similarities.argsort()[::-1][1:top_n+1]
    recommended_rows = reconstructed_df.index[similar_indices]
    return recommended_rows

@app.route('/recommend', methods=['POST'])
@auth.login_required
def recommend():
    data = request.json
    column_name = data['column_name']
    top_n = data.get('top_n', 5)   
    if should_update_data():
         reconstructed_df = load_data_from_mysql()
    else:
        csv_path = 'reconstructed_df.csv'
        reconstructed_df = pd.read_csv(csv_path)
        reconstructed_df.set_index('Family', inplace=True)

    recommended_items = get_recommendations(column_name, reconstructed_df, top_n)

    return jsonify({
        "column_name": column_name,
        "recommended_items": recommended_items.tolist()
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)