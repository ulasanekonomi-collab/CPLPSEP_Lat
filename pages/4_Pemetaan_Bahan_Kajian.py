import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Pemetaan Bahan Kajian PSEP", page_icon="📚", layout="wide")
st.title("📚 Tahap 4: Penurunan CPL ke Bahan Kajian (PBK)")
st.markdown("---")

# 2. Referensi Bahan Kajian Berbasis Draft Revisi 6
st.write("### A. Identifikasi Bahan Kajian (Subject Matter)")
st.info("Bahan Kajian disusun untuk mendukung pencapaian CPL yang telah ditetapkan di Tahap 2.")

# Data Bahan Kajian
pbk_data = {
    "Kelompok Bahan Kajian": [
        "Inti Keilmuan Ekonomi", 
        "Alat Analisis & Kuantitatif", 
        "Ekonomi Kontemporer & Digital", 
        "Nilai Islam & Karakter (M3)", 
        "Ekonomi Sektoral & Wilayah"
    ],
    "Cakupan Materi": [
        "Mikro, Makro, Sejarah Pemikiran Ekonomi, Ekonomi Pembangunan.",
        "Matematika Ekonomi, Ekonometrika, Hamiltonian Dynamics, Statisik.",
        "Ekonomi Digital, Platform Economy, Fintech, Data Analytics.",
        "Akidah, Ibadah, Etika Bisnis Islam, Ekonomi Syariah.",
        "Ekonomi Regional, Perencanaan Wilayah, Circular Loop Integration."
    ]
}
df_pbk = pd.DataFrame(pbk_data)
st.table(df_pbk)

# 3. Matriks Hubungan CPL ke PBK
st.divider()
st.write("### B. Matriks Hubungan CPL -> Bahan Kajian")
st.caption("Tentukan Bahan Kajian mana yang paling dominan mendukung setiap butir CPL.")

# Daftar CPL dari tahap sebelumnya (Simulasi)
cpl_list = ["CPL-S1 (Sikap)", "CPL-P1 (Teori Mikro/Makro)", "CPL-P2 (Ekonomi Digital)", "CPL-K1 (Ekonometrika)", "CPL-K2 (AI/Data Science)"]

# Membuat tabel mapping
mapping_data = {
    "Butir CPL": cpl_list,
    "Bahan Kajian Utama": [
        "Nilai Islam & Karakter (M3)",
        "Inti Keilmuan Ekonomi",
        "Ekonomi Kontemporer & Digital",
        "Alat Analisis & Kuantitatif",
        "Ekonomi Kontemporer & Digital"
    ],
    "Kedalaman (Bloom)": ["C4 - Analisis", "C5 - Evaluasi", "C6 - Kreasi", "C6 - Kreasi", "C6 - Kreasi"]
}

df_mapping = pd.DataFrame(mapping_data)
df_mapping_edited = st.data_editor(df_mapping, use_container_width=True, num_rows="dynamic")

# 4. Analisis Kelengkapan
st.divider()
st.write("### C. Analisis Struktur Kurikulum")
col1, col2 = st.columns(2)

with col1:
    distribusi_pbk = df_mapping_edited["Bahan Kajian Utama"].value_counts()
    st.write("#### Distribusi Bahan Kajian:")
    st.bar_chart(distribusi_pbk)

with col2:
    st.write("#### Rekomendasi Tim Kurikulum:")
    if "Alat Analisis & Kuantitatif" in df_mapping_edited["Bahan Kajian Utama"].values:
        st.success("✅ Aspek Kuantitatif (Hamiltonian/Ekonometrika) sudah terakomodasi.")
    if "Ekonomi Kontemporer & Digital" in df_mapping_edited["Bahan Kajian Utama"].values:
        st.success("✅ Aspek Ekonomi Digital sudah terintegrasi sesuai draf Revisi 6.")

# 5. Tombol Simpan
if st.button("Finalisasi Bahan Kajian"):
    st.balloons()
    st.success("Bahan Kajian telah berhasil dipetakan ke dalam struktur kurikulum!")
