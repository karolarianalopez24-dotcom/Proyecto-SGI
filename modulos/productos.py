import streamlit as st

def mostrar_productos():
    st.header("Catálogo de productos")

    st.write(
        "Conoce nuestra línea de calzado ecológico "
        "elaborado con biocuero vegetal."
    )

    productos = [
        {
            "Producto": "Sandalias de biocuero para adultos",
            "Categoría": "Adultos",
            "Precio": "$37.49"
        },
        {
            "Producto": "Sandalias de biocuero infantiles",
            "Categoría": "Infantil",
            "Precio": "$18.99"
        }
    ]

    st.table(productos)
