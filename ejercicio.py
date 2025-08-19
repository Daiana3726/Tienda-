import pandas as pd
import matplotlib.pyplot as plt
import os

#  Cargar el archivo CSV
df_tienda = pd.read_csv('clientes_electronica.csv')

#  Exploración inicial
print("Primeras 7 filas:\n", df_tienda.head(7))
print("\nÚltimas 3 filas:\n", df_tienda.tail(3))
print("\nColumnas disponibles:\n", df_tienda.columns)
print("\nForma (filas, columnas):\n", df_tienda.shape)
print("\nResumen estadístico:\n", df_tienda.describe())

#  Selección de columnas específicas
print("\nColumnas 'Nombre' y 'Apellido':\n", df_tienda[['Nombre', 'Apellido']])
print("\nColumna 'Producto Comprado':\n", df_tienda['Producto Comprado'])

#  Filtrado por condiciones
print("\nClientes de Rosario:\n", df_tienda[df_tienda['Ciudad'] == 'Rosario'])
print("\nProductos con precios mayor a $1000:\n", df_tienda[df_tienda['Precio Producto'] > 1000])
print("\nClientes con edad menor a 30:\n", df_tienda[df_tienda['Edad'] < 30])

#  Creación de columna 'Venta Total'
df_tienda['Venta Total'] = df_tienda['Precio Producto'] * df_tienda['Cantidad']
print("\nDataFrame con 'Venta Total':\n", df_tienda.head())

#  Agrupaciones
print("\nCantidad total por Producto Comprado:\n",
      df_tienda.groupby('Producto Comprado')['Cantidad'].sum().sort_values(ascending=False))
print("\nPromedio de edad por Ciudad:\n", df_tienda.groupby('Ciudad')['Edad'].mean())
print("\nVenta total por Ciudad:\n", df_tienda.groupby('Ciudad')['Venta Total'].sum().sort_values(ascending=False))

#  Filtrado combinado
print("\nClientes de Mendoza con más de 2 unidades compradas:\n",
      df_tienda[(df_tienda['Ciudad'] == 'Mendoza') & (df_tienda['Cantidad'] > 2)])
print("\nProductos comprados por clientes de Buenos Aires con edad > 40:\n",
      df_tienda[(df_tienda['Ciudad'] == 'Buenos Aires') & (df_tienda['Edad'] > 40)]['Producto Comprado'])

#  Visualización 1: ventas totales por ciudad
ventas_por_ciudad = df_tienda.groupby('Ciudad')['Venta Total'].sum()
plt.figure(figsize=(10, 6))
plt.bar(ventas_por_ciudad.index, ventas_por_ciudad.values)
plt.title('Ventas Totales por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Venta Total')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#  Visualización 2: Top 5 productos más vendidos
productos_mas_vendidos = df_tienda.groupby('Producto Comprado')['Cantidad'].sum().nlargest(5)
plt.figure(figsize=(10, 6))
plt.bar(productos_mas_vendidos.index, productos_mas_vendidos.values)
plt.title('5 Productos Más Vendidos')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.tight_layout()
plt.show()

#  Visualización 3: distribución de clientes por ciudad (top 3)
clientes_por_ciudad = df_tienda['Ciudad'].value_counts().nlargest(3)
plt.figure(figsize=(8, 8))
plt.pie(clientes_por_ciudad.values,
        labels=clientes_por_ciudad.index,
        autopct='%1.1f%%',
        startangle=140)
plt.title('Distribución de Clientes por Ciudad (Top 3)')
plt.axis('equal')
plt.tight_layout()
plt.show()

#  Clasificación por grupos de edad
def asignar_grupo_edad(edad):
    if edad <= 24:
        return 'Menor de 25'
    elif 25 <= edad <= 40:
        return '25-40 años'
    elif 41 <= edad <= 60:
        return '41-60 años'
    else:
        return 'Mayor de 60'

df_tienda['Grupo de Edad'] = df_tienda['Edad'].apply(asignar_grupo_edad)

#  Identificación de los 3 productos más caros
productos_ordenados = df_tienda.groupby('Producto Comprado')['Precio Producto'].mean().sort_values(ascending=False)
productos_mas_caros = productos_ordenados.head(3).index.tolist()

#  Filtrar productos más caros
df_productos_caros = df_tienda[df_tienda['Producto Comprado'].isin(productos_mas_caros)]

#  Agrupación por grupo de edad y producto
ventas_por_grupo_edad = df_productos_caros.groupby(['Grupo de Edad', 'Producto Comprado'])['Venta Total'].sum().unstack()

#  Visualización agrupada
ventas_por_grupo_edad.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas Totales por Grupo de Edad para los Productos Más Caros')
plt.xlabel('Grupo de Edad')
plt.ylabel('Venta Total')
plt.xticks(rotation=45)
plt.legend(title='Producto')
plt.tight_layout()
plt.show()

#  Comentario final
print("El gráfico muestra la distribución de las ventas totales de los productos más caros por grupo de edad.")
print("Se puede observar si ciertos grupos de edad tienen una preferencia por productos específicos o si hay diferencias significativas en las ventas totales entre los grupos.")
print("Por ejemplo, se puede identificar si los clientes más jóvenes tienden a comprar más un producto caro en particular, o si los clientes mayores tienen un patrón de compra diferente.")