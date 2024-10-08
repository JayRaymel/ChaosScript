import streamlit as st
import pandas as pd
import os

# Definimos las categorías permitidas
CATEGORIAS_PERMITIDAS = ['Chocolates', 'Caramelos', 'Mashmelos', 'Galletas', 'Salados', 'Gomas de mascar']
FILE_PATH = 'productos.xlsx'

def cargar_productos():
    """Carga los productos desde un archivo Excel si existe, o retorna una lista vacía."""
    if os.path.exists(FILE_PATH):
        return pd.read_excel(FILE_PATH).to_dict(orient='records')
    return []

def guardar_productos(productos):
    """Guarda la lista de productos en un archivo Excel."""
    try:
        df = pd.DataFrame(productos)
        df.to_excel(FILE_PATH, index=False, engine='openpyxl')
    except ImportError as e:
        st.error(f"Error: El módulo necesario 'openpyxl' no está instalado. Por favor, instale el módulo usando `pip install openpyxl`.")
    except Exception as e:
        st.error(f"Error al guardar el archivo: {e}")

# Cargamos los productos al iniciar la aplicación
productos = cargar_productos()
    
def validar_nombre(nombre):
    """Valida que el nombre del producto no exceda los 20 caracteres."""
    if len(nombre) > 20:
        raise ValueError("El nombre del producto no debe ser mayor a 20 caracteres.")
    return True

def validar_precio(precio):
    """Valida que el precio sea un número mayor a 0 y menor a 999 soles."""
    try:
        precio = float(precio)
        if precio <= 0 or precio >= 999:
            raise ValueError("El precio debe ser mayor a 0 y menor a 999 soles.")
    except ValueError:
        raise ValueError("Por favor verifique el campo del precio. Debe ser un número.")
    return True

def validar_categorias(categorias):
    """Valida que todas las categorías sean válidas."""
    if not all(categoria in CATEGORIAS_PERMITIDAS for categoria in categorias):
        raise ValueError("Una o más categorías no son válidas.")
    return True

def validar_en_venta(en_venta):
    """Valida que el estado de venta sea 'Si' o 'No'."""
    if en_venta not in ['Si', 'No']:
        raise ValueError("El estado de venta debe ser 'Si' o 'No'.")
    return True

def crear_producto(nombre, precio, categorias, en_venta):
    """Valida y guarda un nuevo producto."""
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

# Título de la aplicación
st.title("Formulario de Productos - Confitería Dulcino")

# Entrada de datos
nombre_producto = st.text_input("Nombre del producto")
precio_producto = st.text_input("Precio del producto")
categorias_producto = st.multiselect("Categorías del producto", CATEGORIAS_PERMITIDAS)
en_venta = st.radio("¿El producto está en venta?", ('Si', 'No'))

# Botón para agregar producto
if st.button("Agregar Producto"):
    crear_producto(nombre_producto, precio_producto, categorias_producto, en_venta)

# Mostrar productos agregados
st.subheader("Productos agregados:")
for prod in productos:
    st.write(f"Nombre: {prod['nombre']}, Precio: {prod['precio']}, Categorías: {prod['categorias']}, En venta: {prod['en_venta']}")
