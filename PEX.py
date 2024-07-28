import pandas as pd

data = {
    'Nombre': ['Producto1', 'Producto2'],
    'Precio': [10.0, 15.5]
}
df = pd.DataFrame(data)
df.to_excel('test.xlsx', index=False)
print("Archivo Excel creado exitosamente.")
