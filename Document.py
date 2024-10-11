import streamlit as st
from docx import Document
from datetime import date

# Función para generar un documento
def generar_documento(tipo_documento, nombre, asunto, fecha):
    doc = Document()

    if tipo_documento == "Solicitud":
        doc.add_heading('SOLICITUD', 0)
        doc.add_paragraph(f"Lima, {fecha}")  # Fecha de la solicitud

        # Contenido de la solicitud con espacios para nombres
        doc.add_paragraph(
            f"Señores\n"
            f"Nombre de la institución\n"
            f"Presente.-\n\n"
            f"Yo, {nombre}, por medio de la presente solicito formalmente lo siguiente:\n"
            f"{asunto}\n\n"
            "Agradezco su pronta atención y quedo a la espera de su respuesta."
        )
        
        doc.add_paragraph("\nAtentamente,\n")
        doc.add_paragraph(f"{nombre}")
    else:
        doc.add_heading('OFICIO', 0)
        doc.add_paragraph(f"Lima, {fecha}")  # Fecha del oficio

        # Contenido del oficio
        doc.add_paragraph(
            f"Señores\n"
            f"Nombre de la institución\n"
            f"Presente.-\n\n"
            f"Por la presente, me permito dirigirme a ustedes para informar lo siguiente:\n"
            f"{asunto}\n\n"
            "Sin otro particular, me despido cordialmente, quedando a su disposición."
        )

        doc.add_paragraph("\nAtentamente,\n")
        doc.add_paragraph(f"{nombre}")

    # Guardar el archivo
    nombre_archivo = f'{tipo_documento}_{nombre}.docx'
    doc.save(nombre_archivo)
    return nombre_archivo

# Interfaz de usuario
st.title("Generador de Documentos")

# Obtener datos del usuario
nombre = st.text_input("Nombre")
asunto = st.text_area("Asunto o motivo")
fecha = st.date_input("Fecha", value=date.today())
tipo_documento = st.selectbox("Tipo de Documento", ["Solicitud", "Oficio"])

# Botón para generar el documento
if st.button("Generar Documento"):
    archivo = generar_documento(tipo_documento, nombre, asunto, fecha)
    st.success(f"Documento generado: {archivo}")
    
    # Descargar el documento generado
    with open(archivo, "rb") as file:
        st.download_button(
            label="Descargar Documento",
            data=file,
            file_name=archivo,
            mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

