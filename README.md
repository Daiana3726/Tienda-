README - Análisis de Datos Tienda Electrónicos
¿Qué hace el proyecto?
Análisis completo de datos de ventas de una tienda de electrónicos usando Python. Procesa un archivo CSV con información de clientes y genera reportes y gráficos.
Tecnologías utilizadas:

Python con librerías:

pandas - Para manejar datos
matplotlib - Para crear gráficos
os - Para manejo de archivos



Archivo de datos:

clientes_electronica.csv - Base de datos con ventas de la tienda

Lo que hace el análisis:
1. Exploración básica

Muestra primeras y últimas filas
Información de columnas y tamaño
Estadísticas generales de la tienda

2. Filtrado de datos

Clientes por ciudad (ej: Rosario, Mendoza)
Productos por precio (mayores a $1000)
Clientes por edad (menores de 30)

3. Cálculos nuevos

Creó columna "Venta Total" (Precio × Cantidad)
Agrupaciones por ciudad y producto
Promedios de edad por ciudad

4. Visualizaciones de la tienda

Gráfico 1: Ventas totales por ciudad (barras)
Gráfico 2: Top 5 productos más vendidos (barras)
Gráfico 3: Distribución de clientes por ciudad (torta)
Gráfico 4: Ventas por grupo de edad de productos caros (barras agrupadas)

5. Análisis avanzado

Clasificación por grupos de edad (Menor 25, 25-40, 41-60, Mayor 60)
Identificación de 3 productos más caros de la tienda
Análisis de ventas por edad para productos premium

Funciones principales usadas:

groupby() - Agrupar datos
filter() - Filtrar información
apply() - Aplicar funciones personalizadas
plot() - Crear gráficos
