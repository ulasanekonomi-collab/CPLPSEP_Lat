import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="FEB Unisba Command Center", page_icon="🏢", layout="wide")
st.title("🏢 FEB Unisba Curriculum Command Center")
st.subheader("Instrumen Koordinasi & Supervisi Kurikulum Fakultas")
st.markdown("---")

# 2. Statistik Ringkas (Supervisi Fakultas)
st.write("### 📊 Status Kesiapan Kurikulum OBE")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Prodi EP", "95%", "Revisi 6")
with col2:
    st.metric("Prodi Manajemen", "70%", "-5%", delta_color="normal")
with col3:
    st.metric("Prodi Akuntansi", "85%", "+2%")
with col4:
    st.metric("Rata-rata KKO Tinggi", "78%", "Target 80%")

# 3. Area Otoritas & Supervisi Dekanat
st.divider()
st.write("### 🛡️ Dashboard Otoritas Fakultas")

tab1, tab2, tab3 = st.tabs(["Standardisasi KKO", "Sinkronisasi Profil", "Audit MBKM"])

with tab1:
    st.write("#### Perbandingan Kualitas KKO Antar Prodi")
    # Data simulasi perbandingan antar prodi
    data_kko = pd.DataFrame({
        'Prodi': ['Ekonomi Pembangunan', 'Manajemen', 'Akuntansi'],
        'KKO Analisis (C4)': [30, 25, 35],
        'KKO Evaluasi (C5)': [45, 20, 25],
        'KKO Kreasi (C6)': [25, 15, 10]
    })
    fig_kko = px.bar(data_kko, x='Prodi', y=['KKO Analisis (C4)', 'KKO Evaluasi (C5)', 'KKO Kreasi (C6)'], 
                     title="Distribusi Level Kognitif Kurikulum", barmode='group')
    st.plotly_chart(fig_kko, use_container_width=True)
    st.warning("Catatan Dekanat: Prodi Manajemen perlu meningkatkan porsi KKO C5 dan C6 agar selaras dengan standar fakultas.")

with tab2:
    st.write("#### Kepatuhan Karakter Mujahid, Mujtahid, Mujaddid")
    # Tabel kepatuhan integrasi nilai Islam
    kepatuhan = pd.DataFrame({
        'Aspek Karakter': ['Mujahid (Pejuang)', 'Mujtahid (Peneliti)', 'Mujaddid (Pembaharu)'],
        'PSEP': ["✅ Terintegrasi", "✅ Terintegrasi", "✅ Terintegrasi"],
        'Manajemen': ["✅ Terintegrasi", "⚠️ Parsial", "❌ Belum Terlihat"],
        'Akuntansi': ["✅ Terintegrasi", "✅ Terintegrasi", "⚠️ Parsial"]
    })
    st.table(kepatuhan)

with tab3:
    st.write("#### Peta Kolaborasi MBKM Lintas Prodi FEB")
    st.info("Otoritas fakultas adalah memfasilitasi agar mata kuliah prodi A bisa diambil prodi B secara mulus.")
    st.write("- **Prodi EP:** Menyediakan Paket Regional Development (Siap menerima mhs Manajemen/Akuntansi)")
    st.write("- **Prodi Akuntansi:** Menyediakan Paket Forensic Audit (Siap menerima mhs EP)")

# 4. Panel Persetujuan Dekan
st.divider()
st.write("### ✍️ Panel Validasi & Persetujuan")
prodi_pilihan = st.selectbox("Pilih Kurikulum Prodi untuk di-Review:", ["Ekonomi Pembangunan", "Manajemen", "Akuntansi"])

st.text_area(f"Catatan/Rekomendasi Dekan untuk Prodi {prodi_pilihan}:", "Silakan dilanjutkan ke tahap senat universitas...")

if st.button("Berikan Rekomendasi Fakultas"):
    st.success(f"Rekomendasi untuk {prodi_pilihan} telah dikirim ke Ketua Prodi terkait.")
    st.balloons()

# 5. Footer
st.divider()
st.caption("Fakultas Ekonomi dan Bisnis - Universitas Islam Bandung | Digital Coordination Tools v1.0")
