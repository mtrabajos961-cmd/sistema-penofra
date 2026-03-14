import streamlit as st
from datetime import datetime

st.set_page_config(page_title="PENOFRA C.A.", page_icon="⚡")

st.title("🚀 Sistema de Gestión PENOFRA")
st.write("### Registro de Guías de Movilización")

with st.form("formulario_penofra"):
    col1, col2 = st.columns(2)
    with col1:
        razon = st.text_input("Razón Social")
        atencion = st.text_input("Atención")
        email = st.text_input("Email")
        tlf = st.text_input("Teléfono")
    with col2:
        control = st.text_input("Control Nº")
        entrega = st.text_input("Nota de Entrega")
        fecha = st.date_input("Fecha", datetime.now())
        movil = st.text_input("Móvil")

    st.write("---")
    st.write("### Datos de Transporte")
    chofer = st.text_input("Nombre del Chofer")
    placa = st.text_input("Placa del Vehículo")
    
    if st.form_submit_button("Generar Guía y QR"):
        st.success(f"✅ Guía {control} registrada para {razon}")
        st.info("Conectando con Google Sheets para escribir en F10 y generar QR en F54...")
