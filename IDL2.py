import streamlit as st

# Definimos las categorías permitidas
CATEGORIAS_PERMITIDAS = ['Chocolates', 'Caramelos', 'Mashmelos', 'Galletas', 'Salados', 'Gomas de mascar']

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
