# Optimización de Procesos de Selección de Papas con Base en Datos de Distribución Internacional de Clones: Desarrollo de un Sistema de Sugerencias para Reducir Tiempos de Selección

## 1. Introducción & Antecedentes

Uno de los principales retos en el mejoramiento genético de plantas es la generación de nuevas variedades resistentes a las condiciones climáticas actuales, las cuales son cada vez más variables debido al cambio climático. Además, estas variedades deben desarrollarse en corto tiempo para abordar problemas urgentes como la seguridad alimentaria. Los mejoradores genéticos enfrentan el desafío de tomar decisiones rápidas y precisas al seleccionar el germoplasma adecuado, es decir, elegir el material genético con las características óptimas para generar variedades adaptadas a sus condiciones climáticas específicas, reduciendo así los ensayos de adaptabilidad y estabilidad genética.

## Declaración del Problema

La correcta elección del material genético es crucial para optimizar el tiempo de cultivo y los ensayos de adaptabilidad antes de liberar una variedad para su uso en campo. La ubicación donde se siembra un cultivo puede impactar significativamente en la producción de nuevas variedades. Por ello, el problema a abordar es la selección eficiente de clones de papas adaptables a diferentes condiciones climáticas, utilizando datos históricos y caracterización morfológica para reducir los tiempos y costos en la creación de nuevas variedades.

## Desafíos

El problema es técnicamente desafiante debido a la gran cantidad de datos necesarios para realizar predicciones precisas, la diversidad de condiciones climáticas a nivel mundial y la necesidad de modelos de recomendación robustos que puedan manejar datos esparsos y variables. Además, integrar estos modelos en una plataforma accesible y fácil de usar representa un desafío técnico significativo.

## Trabajos Relacionados

Los trabajos anteriores han abordado estos desafíos mediante el uso de algoritmos de aprendizaje automático y sistemas de recomendación en otras áreas de la agricultura, como la selección de cultivos y pesticidas adecuados. Sin embargo, la mayoría de estos enfoques no han considerado la integración completa de datos morfológicos y de rendimiento con recomendaciones específicas para condiciones climáticas variadas. Nuestro trabajo se basa en estos fundamentos, mejorando la precisión y aplicabilidad del sistema de recomendación.

## 2. Objetivos

1. Desarrollar una plataforma de administración de datos: Crear una herramienta que permita organizar y gestionar de manera eficiente la información sobre clones de papas, incluyendo imágenes, caracterización morfológica y parámetros de rendimiento.
2. Implementar un sistema de recomendación basado en matrix factorization: Utilizar este método para analizar y completar información faltante, optimizando la selección de clones de papas adaptables a diferentes condiciones climáticas.
3. Optimizar la selección de clones de papas para envíos internacionales: Filtrar y recomendar los clones más adecuados para su envío a otros países, basándose en datos históricos de distribución y adaptabilidad a condiciones climáticas similares.
4. Facilitar la toma de decisiones para los mejoradores de papas: Proveer una herramienta que apoye la toma de decisiones basada en datos, ayudando a los mejoradores a seleccionar los mejores clones de papas para su cultivo en nuevas regiones.

## 3. Metodología

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

#### Flujo de trabajo (ver Figura 1)

1. **Recolección de Datos:** Se recopilan datos de materiales de reproducción, liberaciones de variedades en diferentes países y clones avanzados de papas, junto con marcadores SSR y SNP.
2. **Asignación de Puntajes:** Los datos recopilados se utilizan para asignar puntajes a los clones en función de los lugares de envío, el tipo de muestra enviada, la frecuencia de envío, liberación de variedades en los países.
3. **Clasificación de clones relacionados:** Se utilizará la información de caracterización así como las familias del cual se derivan los clones para encontrar clones más cercanamente relacionados pudiendo incorporar en un futuro información de marcadores genéticos.
4. **Factorización de la Matriz:** Se aplica la factorización de matrices (SVD) para completar los datos faltantes y mejorar la matriz de datos.
5. **Sistema de Recomendación:** La matriz de datos factorizada se utiliza para alimentar el sistema de recomendación, desarrollado con Flask, que proporciona recomendaciones de clones óptimos para diferentes regiones.
6. **Integración Web:** La plataforma de administración de datos y el sistema de recomendación se integran en una interfaz web desarrollada con Laravel y MySQL.

![](https://github.com/FranciscoAscue/api-recommend-system-crops/blob/master/FLUJO.png)
_Figura 1: Diagrama del flujo de trabajo que resume la implementación del sistema de recomendación. La figura muestra el procesamiento de la información brindada por el CIP, así como información externa para creación de un sistema de recomendación en Flask y finalmente la interconexión entre Laravel 10 para el backend y MySQL para la base de datos._


## 4. Tu Enfoque y Resultados

### Enfoque Técnico e Innovaciones

Nuestro enfoque técnico se centra en el uso de la Descomposición en Valores Singulares (SVD) para la factorización de matrices y el desarrollo de una API en Flask para integrar el sistema de recomendación con la plataforma de administración de datos. Esta innovación permite una recomendación precisa de clones de papas adaptables a diferentes condiciones climáticas, basándose en datos históricos y caracterización morfológica.

### Resultados de la Evaluación

Hemos evaluado nuestro sistema utilizando un conjunto de datos proporcionado por el Centro Internacional de la Papa (CIP) y datos climáticos de WorldClim. Las métricas de evaluación incluyen precisión en las recomendaciones y reducción en los tiempos de selección de clones. Los resultados han mostrado una mejora significativa en la precisión de las recomendaciones y una reducción considerable en el tiempo de selección, comparado con los métodos tradicionales.

### Impacto de los Resultados

Los resultados obtenidos confirman que el sistema de recomendación basado en SVD y Flask es efectivo y eficiente, superando las expectativas en términos de precisión y tiempo de procesamiento. Esto facilita a los mejoradores genéticos la toma de decisiones informadas y rápidas, optimizando el proceso de desarrollo de nuevas variedades de papas.

## Impacto Más Amplio

### Esperado Impacto del Trabajo

El sistema propuesto permitirá a los mejoradores reducir los costos operativos y mejorar la eficiencia, lo cual puede traducirse en productos finales más económicos y de mejor calidad. Además, optimizará la toma de decisiones mediante la recomendación de clones de papas óptimos basados en datos históricos y características morfológicas y de rendimiento, permitiendo una adaptación más precisa a diferentes condiciones climáticas.

### Aplicabilidad y Lecciones Aprendidas

Esperamos que nuestro trabajo sea aplicado por otros investigadores y mejoradores genéticos para optimizar sus procesos de selección de cultivos. Las técnicas y métodos utilizados pueden adaptarse a otros tipos de cultivos y contextos agrícolas, promoviendo una agricultura más inteligente y sostenible.

### Limitaciones y Futuras Mejoras

Las principales limitaciones de nuestro trabajo incluyen la dependencia de datos históricos y la necesidad de una integración constante de nuevos datos para mantener la precisión del sistema de recomendación. Áreas para futuras mejoras incluyen la incorporación de más métodos de recomendación y el uso de datos en tiempo real para ajustar continuamente las recomendaciones.

## 5. Cronograma

| Semana | Actividades                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| 1      | - Recolección de datos<br> - Desarrollo de la base de datos en MySQL<br> - Configuración de Laravel 10 |
| 2      | - Implementación del backend de la plataforma<br> - Desarrollo del sistema de recomendación en Flask<br> - Integración de SVD y creación de la API de recomendación |
| 3      | - Pruebas y validación del sistema<br> - Integración de la plataforma y el sistema de recomendación<br> - Implementación de la interfaz web y despliegue final |
