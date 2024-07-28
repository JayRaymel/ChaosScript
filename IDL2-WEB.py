import streamlit as st
import pandas as pd
import os

CATEGORIAS_PERMITIDAS = ['Chocolates', 'Caramelos', 'Mashmelos', 'Galletas', 'Salados', 'Gomas de mascar']
FILE_PATH = 'productos.xlsx'

def cargar_productos():
    if os.path.exists(FILE_PATH):
        return pd.read_excel(FILE_PATH).to_dict(orient='records')
    return []

def guardar_productos(productos):
    df = pd.DataFrame(productos)
    df.to_excel(FILE_PATH, index=False)

productos = cargar_productos()

def validar_nombre(nombre):
    if len(nombre) > 20:
        raise ValueError("El nombre del producto no debe ser mayor a 20 caracteres.")
    return True

def validar_precio(precio):
    try:
        precio = float(precio)
        if precio <= 0 or precio >= 999:
            raise ValueError("El precio debe ser mayor a 0 y menor a 999 soles.")
    except ValueError:
        raise ValueError("Por favor verifique el campo del precio. Debe ser un número.")
    return True

def validar_categorias(categorias):
    if not all(categoria in CATEGORIAS_PERMITIDAS for categoria in categorias):
        raise ValueError("Una o más categorías no son válidas.")
    return True

def validar_en_venta(en_venta):
    if en_venta not in ['Si', 'No']:
        raise ValueError("El estado de venta debe ser 'Si' o 'No'.")
    return True

def crear_producto(nombre, precio, categorias, en_venta):
    try:
        validar_nombre(nombre)
        validar_precio(precio)
        validar_categorias(categorias)
        validar_en_venta(en_venta)
        producto = {
            'nombre': nombre,
            'precio': precio,
            'categorias': ', '.join(categorias),
            'en_venta': en_venta
        }
        productos.append(producto)
        guardar_productos(productos)
        st.success("Felicidades, su producto se agregó.")
    except ValueError as e:
        st.error(f"Lo sentimos, no pudo crear este producto. Error: {e}")

st.title("Formulario de Productos - Confitería Dulcino")

nombre_producto = st.text_input("Nombre del producto")
precio_producto = st.text_input("Precio del producto")
categorias_producto = st.multiselect("Categorías del producto", CATEGORIAS_PERMITIDAS)
en_venta = st.radio("¿El producto está en venta?", ('Si', 'No'))

if st.button("Agregar Producto"):
    crear_producto(nombre_producto, precio_producto, categorias_producto, en_venta)

st.subheader("Productos agregados:")
for prod in productos:
    st.write(f"Nombre: {prod['nombre']}, Precio: {prod['precio']}, Categorías: {prod['categorias']}, En venta: {prod['en_venta']}")
