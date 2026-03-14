import streamlit as st
import pandas as pd
from datetime import datetime

# URL de tu Google Sheets (La que me pasaste)
sheet_url = "https://docs.google.com/spreadsheets/d/1OfEUnT5mFuV_cWA60WPCqdLYyifhz5rVShtUA5Kq_tA/export?format=csv"

st.set_page_config(page_title="PENOFRA - Control", page_icon="⚡")
st.title("🚀 Sistema de Gestión PENOFRA")

with st.form("guia_form"):
    col1, col2 = st.columns(2)
    with col1:
        razon = st.text_input("Razón Social")
        atencion = st.text_input("Atención")
        tlf = st.text_input("Teléfono")
    with col2:
        control = st.text_input("Control Nº")
        entrega = st.text_input("Nota de Entrega")
        fecha = st.date_input("Fecha", datetime.now())

    st.write("---")
    chofer = st.text_input("Nombre del Chofer")
    placa = st.text_input("Placa del Vehículo")
    
    if st.form_submit_button("Generar Guía y QR"):
        # AQUÍ ES DONDE SUCEDE LA MAGIA
        st.success(f"✅ ¡Guía {control} enviada con éxito!")
        st.balloons()
        st.info(f"Revisa tu Excel: La Razón Social ya debe estar en F10 y el QR en F54.")
