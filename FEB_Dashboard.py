import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FEB Unisba Command Center", page_icon="🏢", layout="wide")
st.title("🏢 FEB Unisba Curriculum Command Center")
st.subheader("Instrumen Koordinasi & Supervisi Kurikulum Fakultas")
st.markdown("---")

# Ringkasan Kesiapan
st.write("### 📊 Status Kesiapan Kurikulum OBE")
col1, col2, col3 = st.columns(3)
col1.metric("Prodi EP", "95%", "Revisi 6")
col2.metric("Prodi Manajemen", "70%", "Perlu Review")
col3.metric("Prodi Akuntansi", "85%", "Finalisasi")

# Grafik KKO (High Order Thinking)
st.divider()
st.write("### 🛡️ Dashboard Otoritas Fakultas")
data_kko = pd.DataFrame({
    'Prodi': ['EP', 'Manajemen', 'Akuntansi'],
    'KKO Tinggi (C4-C6)': [78, 45, 60],
    'KKO Menengah (C1-C3)': [22, 55, 40]
})
fig = px.bar(data_kko, x='Prodi', y=['KKO Tinggi (C4-C6)', 'KKO Menengah (C1-C3)'], barmode='group')
st.plotly_chart(fig, use_container_width=True)

# Panel Persetujuan Dekan
st.divider()
prodi = st.selectbox("Review Prodi:", ["Ekonomi Pembangunan", "Manajemen", "Akuntansi"])
st.text_area(f"Catatan Dekan untuk {prodi}:", "Dokumen sesuai standar OBE.")
if st.button("Kirim Validasi Fakultas"):
    st.balloons()
    st.success("Rekomendasi Terkirim!")
