# BehaviorTracker

Proyecto programacion I



* Descripción del proyecto



Este proyecto tiene como objetivo desarrollar un sistema capaz de procesar y analizar datos de uso de aplicaciones móviles. A partir de un archivo de datos en formato CSV, el sistema permite organizar la información, filtrarla por participante y calcular métricas básicas de uso.



El trabajo se enmarca en el análisis del comportamiento digital, considerando variables como la frecuencia de uso y el tiempo dedicado a distintas aplicaciones.



* Objetivos
1. Leer y estructurar datos desde un archivo externo

2\. Almacenar los datos en memoria de manera organizada

3\. Filtrar información por participante

4\. Calcular métricas básicas de uso

5\. Generar resultados claros a partir de los datos



* Estructura del proyecto

BehaviorTracker/

│

├── main.py

├── src/

│   ├── \_\_init\_\_.py

│   ├── carga\_datos.py

│   ├── procesamiento\_datos.py

│   ├── metricas.py

│   └── validacion\_datos.py

│

└── datos/

&#x20;   └── datos.csv



* Funcionamiento del sistema
1. Carga de datos: se lee un archivo CSV que contiene los registros de uso de aplicaciones.

2\. Estructuración: los datos se almacenan en un diccionario de listas, donde cada clave representa una variable.

3\. Interacción con el usuario: el usuario ingresa el ID de un participante.

4\. Filtrado de datos: se seleccionan únicamente los registros correspondientes a ese participante.

5\. Cálculo de métricas

Tiempo total de uso:

Promedio de uso

6\. Visualización de resultados: se muestran los resultados por consola.



* Formato de los datos (datos.csv)

id\_participante,fecha,app,cantidad\_uso,tiempo\_uso



Ejemplo:

1,2024-04-01,Instagram,5,120

1,2024-04-01,WhatsApp,3,60



* Autores

Delfina Guirao, Josefina Hermida, Leila Mena, Emilia Welyczko

