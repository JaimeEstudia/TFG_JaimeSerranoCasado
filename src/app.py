import streamlit as st
from main import main


def app():
    st.set_page_config(page_title="Evaluador de proyectos", layout="centered")

    st.title("Evaluador inteligente de proyectos")

    st.markdown(
        "Sube la **rúbrica de evaluación** y el **archivo de código** para iniciar el análisis."
    )

    # Subida de los archivos
    rubrica_file = st.file_uploader("Rúbrica (TXT)", type=["txt"], key="rubrica")

    codigo_file = st.file_uploader("Código (PY)", type=["py"], key="codigo")

    # Botón de ejecución
    if st.button("Ejecutar evaluación", disabled=not (rubrica_file and codigo_file)):
        with st.spinner("Evaluando proyecto..."):
            resultado = main(
                rubrica_file.read().decode("utf-8"), codigo_file.read().decode("utf-8")
            )

        st.success("Evaluación completada")

        st.subheader("Resultado:")
        st.text(resultado)


if __name__ == "__main__":
    app()
