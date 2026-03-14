import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración visual
st.set_page_config(page_title="PENOFRA - Gestión de Guías", page_icon="⚡", layout="centered")

# Estilo personalizado (Azul Corporativo)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-title { color: #004a99; font-weight: bold; text-align: center; }
    .section-box { border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Logo de la empresa
st.image("https://raw.githubusercontent.com/mtrabajos961-cmd/sistema-penofra/main/1773415300096.jpg", width=200)
st.markdown("<h1 class='main-title'>CORPORACIÓN PNF, C.A.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>RIF J-50150706-6</p>", unsafe_allow_html=True)

st.write("---")

# Tasa del día (BCV)
tasa_bcv = st.sidebar.number_input("Tasa BCV (Bs/USD)", value=36.50, step=0.01)

# FORMULARIO
with st.container():
    st.subheader("📋 Datos de la Guía")
    col1, col2 = st.columns(2)
    with col1:
        control = st.text_input("Control Nº", placeholder="0001")
        razon = st.text_input("Razón Social / Cliente")
        tlf = st.text_input("Teléfono")
    with col2:
        entrega = st.text_input("Nota de Entrega")
        atencion = st.text_input("Atención a")
        fecha = st.date_input("Fecha", datetime.now())

    st.write("---")
    st.subheader("⚙️ Detalles del Equipo")
    col3, col4 = st.columns(2)
    descripcion = col3.text_area("Descripción del Equipo", placeholder="Ej: Transformador 25 KVA...")
    serial = col4.text_input("Serial del Equipo")
    
    costo_usd = st.number_input("Costo del Servicio (USD)", min_value=0.0, step=1.0)
    
    # Cálculos automáticos
    iva_usd = costo_usd * 0.16
    total_usd = costo_usd + iva_usd
    total_bs = total_usd * tasa_bcv

    st.write("---")
    st.subheader("🚛 Datos de Transporte")
    c5, c6 = st.columns(2)
    chofer = c5.text_input("Nombre del Chofer")
    placa = c6.text_input("Placa del Vehículo")

# BOTÓN DE ACCIÓN
if st.button("✅ GENERAR GUÍA Y REGISTRAR EN EXCEL"):
    if not razon or not control:
        st.error("Mano, pon al menos el Control y la Razón Social.")
    else:
        st.success(f"¡Guía {control} procesada con éxito!")
        
        # Resumen estilo "Hoja de Excel"
        st.markdown(f"""
        <div style="border: 2px solid #004a99; padding: 20px; border-radius: 5px;">
            <h4>RESUMEN DE FACTURACIÓN (Tasa: {tasa_bcv} Bs)</h4>
            <p><b>Subtotal:</b> {costo_usd:,.2f} $</p>
            <p><b>IVA (16%):</b> {iva_usd:,.2f} $</p>
            <hr>
            <p style="font-size: 20px;"><b>TOTAL A PAGAR:</b> {total_usd:,.2f} $ / <b>{total_bs:,.2f} Bs</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info(f"Escribiendo en celda F10 para {razon}...")
        st.balloons()
