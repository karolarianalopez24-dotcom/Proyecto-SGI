import streamlit as st
from modulos.login import login
from modulos.VENTAS import mostrar_venta
from modulos.productos import mostrar_productos

# Inicializar variables de sesion
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False

if "usuario" not in st.session_state:
    st.session_state["usuario"] = ""

# Comprobar si el usuario inicio sesion
if st.session_state["sesion_iniciada"]:

    st.sidebar.title("Menú")

    st.sidebar.write(
        f"Usuario: {st.session_state['usuario']}"
    )

    # Opciones del menu lateral
    opciones = [
        "Ventas",
        "Productos",
        "Información"
    ]

    seleccion = st.sidebar.selectbox(
        "Seleccione una opción",
        opciones
    )

    # Modulo de Ventas
    if seleccion == "Ventas":
        mostrar_venta()

    # Modulo de Productos
    elif seleccion == "Productos":
        mostrar_productos()

    # Modulo de Informacion
    elif seleccion == "Información":

        st.header("Información del sistema")

        st.write(
            "Sistema de Gestión de Información para "
            "las tiendas minoristas y el Centro de Distribución "
            "de la Cooperativa de Mujeres de Occidente."
        )

        st.subheader("Áreas del sistema")

        st.write(
            "**Tiendas minoristas:** permiten registrar "
            "ventas y consultar los productos disponibles."
        )

        st.write(
            "**Centro de Distribución:** se encarga de "
            "organizar el abastecimiento de productos "
            "hacia las diferentes tiendas minoristas."
        )

        st.write(
            "**Proveedores:** suministran los productos "
            "que posteriormente serán distribuidos "
            "a las tiendas."
        )

        st.subheader("Objetivo del sistema")

        st.write(
            "Facilitar la gestión de la información "
            "relacionada con las ventas, productos "
            "y abastecimiento de las tiendas minoristas."
        )

        st.info(
            "Esta aplicación es un prototipo académico "
            "desarrollado para el Laboratorio de "
            "Sistemas de Gestión de la Información."
        )

    # Cerrar sesion
    if st.sidebar.button("Cerrar sesión"):
        st.session_state["sesion_iniciada"] = False
        st.session_state["usuario"] = ""
        st.rerun()

else:
    # Mostrar inicio de sesion
    login()


