# Optimización de Procesos de Selección de Papas con Base en Datos de Distribución Internacional de Clones: Desarrollo de un Sistema de Sugerencias para Reducir Tiempos de Selección

## 1. Introducción & Antecedentes

Uno de los principales retos en el mejoramiento genético de plantas es la generación de nuevas variedades resistentes a las condiciones climáticas actuales, las cuales son cada vez más variables debido al cambio climático. Además, estas variedades deben desarrollarse en corto tiempo para abordar problemas urgentes como la seguridad alimentaria. Los mejoradores genéticos enfrentan el desafío de tomar decisiones rápidas y precisas al seleccionar el germoplasma adecuado, es decir, elegir el material genético con las características óptimas para generar variedades adaptadas a sus condiciones climáticas específicas, reduciendo así los ensayos de adaptabilidad y estabilidad genética.

El mejoramiento tradicional de la papa ha sido una práctica esencial en la agricultura durante siglos. Este proceso consiste en la selección y cruce de variedades de papa con características deseadas, tales como resistencia a enfermedades, adaptación a diferentes condiciones climáticas, y mejora en la calidad y rendimiento de los tubérculos. Mediante la selección de plantas con los mejores atributos y su reproducción, los agricultores han logrado desarrollar variedades que no solo se adaptan mejor a las condiciones locales, sino que también ofrecen mayores beneficios económicos y nutricionales.

Históricamente, los métodos de mejoramiento han dependido en gran medida de la observación y la experiencia acumulada de los agricultores, quienes identifican y guardan las mejores semillas de cada cosecha. Este enfoque empírico ha sido fundamental para la diversificación y la adaptación de la papa en diversas regiones del mundo. Hoy en día, aunque existen técnicas modernas de mejoramiento genético, el mejoramiento tradicional sigue siendo una herramienta valiosa, especialmente en regiones donde el acceso a la biotecnología es limitado.

## 2. Declaración del Problema

La correcta elección del material genético es crucial para optimizar el tiempo de cultivo y los ensayos de adaptabilidad antes de liberar una variedad para su uso en campo. La ubicación donde se siembra un cultivo puede impactar significativamente en la producción de nuevas variedades. Por ello, el problema a abordar es la selección eficiente de clones de papas adaptables a diferentes condiciones climáticas, utilizando datos históricos y caracterización morfológica para reducir los tiempos y costos en la creación de nuevas variedades

## 3. Desafíos

El problema es técnicamente desafiante debido a la gran cantidad de datos necesarios para realizar predicciones precisas, la diversidad de condiciones climáticas a nivel mundial y la necesidad de modelos de recomendación robustos que puedan manejar datos esparsos y variables. Además, integrar estos modelos en una plataforma accesible y fácil de usar representa un desafío técnico significativo.

## 4. Trabajos Relacionados

Los trabajos anteriores han abordado estos desafíos mediante el uso de algoritmos de aprendizaje automático y sistemas de recomendación en otras áreas de la agricultura, como la selección de cultivos y pesticidas adecuados. Por ejemplo, Paudel et al. (2021) emplearon una combinación de modelos de cultivo y aprendizaje automático para predecir el rendimiento de los cultivos, utilizando datos de simulación de cultivos, clima, teledetección y suelos. Este enfoque modular y reutilizable mostró alta precisión en la predicción de rendimientos de cultivos a gran escala​ (SpringerLink)​.

Sun et al. (2020) utilizaron técnicas como Gradient Boosting, Support Vector Regression (SVR) y k-Nearest Neighbors para predecir los rendimientos de varios cultivos, incluyendo papas, en diferentes países europeos. Su modelo de aprendizaje profundo combinó redes neuronales recurrentes (RNN) y convolucionales (CNN) para extraer características espaciales y temporales, mejorando significativamente la precisión de las predicciones en comparación con modelos tradicionales​ (SpringerLink)​.

Khaki y Wang (2018) desarrollaron una solución basada en redes neuronales profundas para predecir el rendimiento de híbridos de maíz, utilizando datos de genotipos y medioambientales. Sus modelos mostraron una alta precisión al integrar variables de simulación de cultivos y datos meteorológicos, reduciendo el error de predicción del rendimiento hasta en un 20%​ (SpringerLink)​.

En el ámbito específico de la recomendación de cultivos, Suresh et al. (2021) implementaron un sistema de recomendación eficiente basado en el aprendizaje automático para la agricultura digital, utilizando atributos de suelos y datos históricos para sugerir cultivos óptimos según las condiciones específicas de cada región. Este enfoque integró múltiples fuentes de datos para proporcionar recomendaciones personalizadas y precisas​ (SpringerLink)​.

Patel y Patel (2020) realizaron una revisión exhaustiva de los sistemas de recomendación y sus extensiones prospectivas en la agricultura, destacando la integración de datos morfológicos y de rendimiento con recomendaciones específicas para condiciones climáticas variadas. Identificaron que la mayoría de los sistemas de recomendación actuales no consideraban completamente esta integración, lo que limita su aplicabilidad y precisión en escenarios reales​ (SpringerLink)​.

Estos estudios proporcionan una base sólida para la integración de algoritmos de aprendizaje automático y sistemas de recomendación en el proceso de selección de clones de papas, mejorando la precisión y aplicabilidad del sistema de recomendación propuesto en nuestro trabajo.

## 5. Objetivos

1. Desarrollar una plataforma de administración de datos: Crear una herramienta que permita organizar y gestionar de manera eficiente la información sobre clones de papas, incluyendo imágenes, caracterización morfológica y parámetros de rendimiento.
2. Implementar un sistema de recomendación basado en matrix factorization: Utilizar este método para analizar y completar información faltante, optimizando la selección de clones de papas adaptables a diferentes condiciones climáticas.
3. Optimizar la selección de clones de papas para envíos internacionales: Filtrar y recomendar los clones más adecuados para su envío a otros países, basándose en datos históricos de distribución y adaptabilidad a condiciones climáticas similares.
4. Facilitar la toma de decisiones para los mejoradores de papas: Proveer una herramienta que apoye la toma de decisiones basada en datos, ayudando a los mejoradores a seleccionar los mejores clones de papas para su cultivo en nuevas regiones.

## 6. Metodología

### Desarrollo de la Plataforma de Administración de Datos

Para construir el backend de nuestra plataforma de administración de datos, utilizaremos Laravel 10, un framework PHP que facilita el desarrollo ágil de aplicaciones web robustas y seguras. La base de datos será MySQL, que se integrará con Laravel para permitir una gestión eficiente de las operaciones CRUD disponibles en la plataforma web.

La base de datos almacenará información relevante sobre los clones de papas, incluyendo datos de envíos anteriores, caracterización morfológica, parámetros de rendimiento, y datos de usuarios. El sistema permitirá diferentes niveles de permisos para usuarios, incluyendo:
- **Administrador:** Tendrá control total sobre la plataforma y la gestión de los usuarios.
- **Usuario de Edición:** Podrá manejar y actualizar los datos de los clones de papas.
- **Usuario de Consulta:** Podrá realizar búsquedas avanzadas y mantener un historial de consultas.

Además, esta plataforma estará integrada con otras funcionalidades, como el sistema de recomendación, optimizando así la gestión y análisis de datos para mejorar la toma de decisiones en el mejoramiento genético de plantas.

### Implementación del Sistema de Recomendación

Para el sistema de recomendación, se utilizará el método de descomposición en valores singulares (SVD):

- **SVD (Descomposición en Valores Singulares):** Utilizaremos SVD para descomponer la matriz de datos en productos de matrices menores, identificando relaciones latentes entre los clones de papas y sus características, lo que permitirá realizar recomendaciones precisas.

El sistema de recomendación se implementará como una API que se integrará con la plataforma principal. Utilizaremos Flask, un framework ligero de Python, para desarrollar y desplegar los modelos de recomendación. La API de recomendación desarrollada con Flask se integrará en la plataforma a través de endpoints que permitirán la búsqueda y filtrado de clones de papas óptimos para su envío a diferentes países.

#### Flujo de trabajo

1. **Recolección de Datos:** Se recopilan datos de materiales de reproducción, liberaciones de variedades en diferentes países y clones avanzados de papas, junto con marcadores SSR y SNP.
2. **Asignación de Puntajes:** Los datos recopilados se utilizan para asignar puntajes a los clones en función de los lugares de envío, el tipo de muestra enviada, la frecuencia de envío, liberación de variedades en los países.
3. **Factorización de la Matriz:** Se aplica la factorización de matrices (SVD) para completar los datos faltantes y mejorar la matriz de datos.
4. **Sistema de Recomendación:** La matriz de datos factorizada se utiliza para alimentar el sistema de recomendación, desarrollado con Flask, que proporciona recomendaciones de clones óptimos para diferentes regiones.
5. **Integración Web:** La plataforma de administración de datos y el sistema de recomendación se integran en una interfaz web desarrollada con Laravel y MySQL.

![Diagrama de flujo](https://github.com/FranciscoAscue/api-recommend-system-crops/blob/master/FLUJO.png)
_Figura 1: Diagrama del flujo de trabajo que resume la implementación del sistema de recomendación. La figura muestra el procesamiento de la información brindada por el CIP, así como información externa para creación de un sistema de recomendación en Flask y finalmente la interconexión entre Laravel 10 para el backend y MySQL para la base de datos._

### Diagrama Entidad-Relación (ERD)

El siguiente diagrama entidad-relación (ERD) muestra la estructura de la base de datos utilizada en la plataforma de administración de datos. Este diagrama representa las entidades principales y sus relaciones, facilitando la comprensión de cómo se organiza y gestiona la información sobre los clones de papas.

![Diagrama ERD](https://github.com/FranciscoAscue/api-recommend-system-crops/blob/master/DATABASE.png)
_Figura 2: Diagrama entidad-relación (ERD) de la base de datos utilizada en la plataforma. Las entidades principales incluyen usuarios, países, envíos, clones, variedades, características de clones y recomendaciones._

## 7. Enfoque y Resultados


## Impacto Más Amplio

### Esperado Impacto del Trabajo

El sistema propuesto permitirá a los mejoradores reducir los costos operativos y mejorar la eficiencia, lo cual puede traducirse en productos finales más económicos y de mejor calidad. Además, optimizará la toma de decisiones mediante la recomendación de clones de papas óptimos basados en datos históricos y características morfológicas y de rendimiento, permitiendo una adaptación más precisa a diferentes condiciones climáticas.

### Aplicabilidad y Lecciones Aprendidas

Esperamos que nuestro trabajo sea aplicado por otros investigadores y mejoradores genéticos para optimizar sus procesos de selección de cultivos. Las técnicas y métodos utilizados pueden adaptarse a otros tipos de cultivos y contextos agrícolas, promoviendo una agricultura más inteligente y sostenible.

### Limitaciones y Futuras Mejoras

Las principales limitaciones de nuestro trabajo incluyen la dependencia de datos históricos y la necesidad de una integración constante de nuevos datos para mantener la precisión del sistema de recomendación. Áreas para futuras mejoras incluyen la incorporación de más métodos de recomendación y el uso de datos en tiempo real para ajustar continuamente las recomendaciones.

## 8. Cronograma

| Semana | Actividades                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| 1      | - Recolección de datos<br> - Desarrollo de la base de datos en MySQL<br> - Configuración de Laravel 10 |
| 2      | - Implementación del backend de la plataforma<br> - Desarrollo del sistema de recomendación en Flask<br> - Integración de SVD y creación de la API de recomendación |
| 3      | - Pruebas y validación del sistema<br> - Integración de la plataforma y el sistema de recomendación<br> - Implementación de la interfaz web y despliegue final |
