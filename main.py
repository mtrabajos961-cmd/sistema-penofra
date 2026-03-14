import streamlit as st
from datetime import datetime

st.set_page_config(page_title="PENOFRA C.A.", layout="wide")

# Estilo para que se parezca a tu formato
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #004a99; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Generador de Guías - Corporación PNF")

# --- BLOQUE 1: DATOS DE CABECERA ---
with st.expander("1. Datos del Cliente y Control", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        razon = st.text_input("Razón Social / Cliente")
        atencion = st.text_input("Atención a:")
        tlf = st.text_input("Teléfonos")
    with col2:
        control = st.text_input("Control Nº", placeholder="Ej: 00145")
        entrega = st.text_input("Nota de Entrega Nº")
        fecha = st.date_input("Fecha de Salida", datetime.now())

# --- BLOQUE 2: TABLA DE EQUIPOS ---
st.subheader("2. Equipos a Movilizar")
if 'filas' not in st.session_state:
    st.session_state.filas = 1

def agregar_fila(): st.session_state.filas += 1

for i in range(st.session_state.filas):
    c1, c2, c3, c4 = st.columns([1, 3, 2, 2])
    c1.text(f"Item {i+1}")
    c2.text_input("Descripción / Modelo", key=f"desc_{i}")
    c3.text_input("Serial", key=f"serial_{i}")
    c4.number_input("Costo (USD)", key=f"costo_{i}", min_value=0.0)

st.button("➕ Agregar otro equipo", on_click=agregar_fila)

# --- BLOQUE 3: TRANSPORTE Y LOGÍSTICA ---
with st.expander("3. Datos de Logística"):
    c1, c2, c3 = st.columns(3)
    chofer = c1.text_input("Nombre del Chofer")
    placa = c2.text_input("Placa Vehículo")
    destino = c3.text_input("Destino")

# --- BLOQUE 4: CÁLCULOS ---
st.write("---")
tasa = st.number_input("Tasa BCV (Bs/USD)", value=36.50) # Puedes ajustarla diario

if st.button("🚀 GENERAR GUÍA OFICIAL Y QR"):
    # Aquí simulamos la escritura en las celdas F10, F54, etc.
    st.success(f"¡Guía {control} procesada!")
    
    # Muestra un resumen estilo factura
    st.info(f"**Cliente:** {razon} | **Total USD:** Calculando... | **Total Bs:** Calculando...")
    st.warning("Escribiendo datos en Google Sheets... El QR se pegará en F54:F58")
    st.balloons()
