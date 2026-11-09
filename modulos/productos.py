import streamlit as st

def mostrar_productos():
    st.header("Catálogo de productos")

    st.write(
        "Sistema de Gestión de Tiendas Minoristas "
        "de la Cooperativa de Mujeres de Occidente."
    )

    st.subheader("Productos disponibles")

    productos = [
        {
            "Producto": "Arroz",
            "Categoría": "Granos básicos",
            "Unidad": "Libra"
        },
        {
            "Producto": "Frijoles",
            "Categoría": "Granos básicos",
            "Unidad": "Libra"
        },
        {
            "Producto": "Aceite vegetal",
            "Categoría": "Aceites",
            "Unidad": "Botella"
        }
    ]

    st.table(productos)

    st.info(
        "Este catálogo es utilizado por las tiendas "
        "minoristas y el Centro de Distribución "
        "para la gestión de productos."
    )
