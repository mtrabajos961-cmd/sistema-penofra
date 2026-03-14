import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import qrcode
from io import BytesIO

# --- CONFIGURACIÓN DE GOOGLE SHEETS ---
# (Mano, para el siguiente paso necesito que me pases un archivo JSON que vamos a crear)
def conectar_excel():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Intentaremos conectar con secretos de Streamlit para que sea seguro
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
        client = gspread.authorize(creds)
        # Usamos el ID de tu hoja que saqué de tu link
        sheet = client.open_by_key("1OfEUnT5mFuV_cWA60WPCqdLYyifhz5rVShtUA5Kq_tA").sheet1
        return sheet
    except:
        return None

# --- DISEÑO DE LA APP ---
st.set_page_config(page_title="PENOFRA - Facturación", layout="centered")
st.image("logo.png", width=200)
st.title("Sistema de Control PENOFRA")

tasa = st.sidebar.number_input("Tasa BCV", value=36.50)

with st.form("guia_real"):
    c1, c2 = st.columns(2)
    control = c1.text_input("Control Nº")
    razon = c2.text_input("Razón Social (Celda F10)")
    
    c3, c4 = st.columns(2)
    serial = c3.text_input("Serial del Equipo (Celda E22)")
    costo = c4.number_input("Costo USD", min_value=0.0)
    
    if st.form_submit_button("ENVIAR A EXCEL Y GENERAR QR"):
        sheet = conectar_excel()
        if sheet:
            # Escribir en las celdas exactas de tu formato
            sheet.update_acell('F10', razon)
            sheet.update_acell('E22', serial)
            # El QR se genera basado en el Control
            st.success(f"✅ ¡Listo! Datos de {razon} enviados al formato.")
        else:
            st.warning("⚠️ App lista, pero falta la 'llave' (JSON) para entrar al Excel.")
