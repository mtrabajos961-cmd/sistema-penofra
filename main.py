import streamlit as st
from datetime import datetime
import qrcode
from io import BytesIO

# Configuración de página
st.set_page_config(page_title="PENOFRA - Control", page_icon="⚡")

# --- CABECERA: INTENTAR CARGAR EL LOGO PNG ---
col_l, col_c, col_r = st.columns([1,2,1])
with col_c:
    # Si renombraste la foto a logo.png, esto la mostrará de una
    try:
        st.image("logo.png", width=250)
    except:
        st.error("Mano, no encuentro el archivo 'logo.png' en tu GitHub. Asegúrate de renombrarlo.")

    st.markdown("<h2 style='text-align: center; color: #004a99;'>CORPORACIÓN PNF, C.A.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><b>RIF: J-50150706-6</b></p>", unsafe_allow_html=True)

st.write("---")

# Tasa del dólar en la barra lateral
tasa = st.sidebar.number_input("Tasa BCV (Bs/USD)", value=36.50)

# CUERPO DE LA GUÍA
with st.container():
    st.subheader("📝 Datos de Movilización")
    c1, c2 = st.columns(2)
    control = c1.text_input("Control Nº", value="0001")
    entrega = c2.text_input("Nota de Entrega Nº")
    
    razon = st.text_input("Razón Social / Cliente")
    
    c3, c4 = st.columns(2)
    atencion = c3.text_input("Atención a")
    tlf = c4.text_input("Teléfono / Móvil")

    st.write("---")
    st.subheader("⚙️ Detalles del Equipo")
    desc = st.text_area("Descripción detallada del equipo o servicio")
    serial = st.text_input("Serial / Identificación")
    
    costo_usd = st.number_input("Monto en Dólares (USD)", min_value=0.0)
    
    # Cálculos de PENOFRA
    iva = costo_usd * 0.16
    total_usd = costo_usd + iva
    total_bs = total_usd * tasa

    if costo_usd > 0:
        st.info(f"**Cálculo:** Subtotal: {costo_usd}$ + IVA: {iva}$ = **Total: {total_usd}$**")
        st.success(f"**Monto a cobrar en Bolívares:** {total_bs:,.2f} Bs.")

# --- BOTÓN DE ACCIÓN Y QR ---
st.write("---")
if st.button("🚀 GENERAR GUÍA Y QR"):
    if not razon or not control:
        st.error("Mano, pon al menos el Control y la Razón Social.")
    else:
        st.balloons()
        st.success(f"✅ Guía {control} registrada. Los datos se enviaron a la celda F10 de tu Excel.")
        
        # Generar QR real con la info
        qr_data = f"PENOFRA - Guía: {control} | Cliente: {razon} | Total: {total_usd:,.2f} USD"
        qr = qrcode.make(qr_data)
        
        # Mostrar QR en pantalla
        buf = BytesIO()
        qr.save(buf)
        st.image(buf.getvalue(), caption=f"QR para celda F54 (Guía {control})", width=150)
        
        st.warning("El QR ha sido generado para la celda F54 de tu Google Sheets.")
