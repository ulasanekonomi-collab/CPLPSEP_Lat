import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="OBLT & OBAE PSEP", page_icon="⚖️", layout="wide")
st.title("⚖️ Tahap 7: Sistem OBLT & OBAE")
st.markdown("---")

# 2. Modul OBLT (Learning & Teaching)
st.write("### A. Outcome Based Learning & Teaching (OBLT)")
st.info("Pilih metode pembelajaran yang selaras dengan taksonomi CPL.")

col1, col2 = st.columns(2)

with col1:
    mk_pilihan = st.selectbox("Pilih Mata Kuliah untuk Simulasi:", 
                             ["Ekonometrika Hamiltonian", "Ekonomi Digital", "Etika Bisnis Islam"])
    
    metode = st.multiselect("Metode Pembelajaran (OBLT):", 
                           ["Case-Based Method (CBM)", "Project-Based Learning (PjBL)", "Simulasi Laboratorium", "Discovery Learning", "Ceramah Interaktif"])

with col2:
    st.write("#### 🎯 Aktivitas Mahasiswa:")
    if "Project-Based Learning (PjBL)" in metode:
        st.write("- Menyusun model ekonomi dinamis berbasis data riil.")
    if "Case-Based Method (CBM)" in metode:
        st.write("- Menganalisis kegagalan kebijakan pasar digital di Indonesia.")

# 3. Modul OBAE (Assessment & Evaluation)
st.divider()
st.write("### B. Outcome Based Assessment & Evaluation (OBAE)")

# Data Editor untuk Komponen Penilaian
st.write("#### Matriks Penilaian Berbasis CPL:")
assessment_data = {
    "Komponen Penilaian": ["Tugas Mandiri", "Ujian Tengah Semester", "Proyek Akhir", "Partisipasi Kelas"],
    "Bobot (%)": [20, 30, 40, 10],
    "CPL yang Diukur": ["CPL-P1", "CPL-K1", "CPL-K2", "CPL-S1"],
    "Instrumen": ["Rubrik Analisis", "Soal Kasus", "Rubrik Produk", "Logbook Keaktifan"]
}

df_assessment = pd.DataFrame(assessment_data)
df_ev = st.data_editor(df_assessment, use_container_width=True)

# 4. Evaluasi Ketercapaian (Closing the Loop)
st.divider()
st.write("### C. Analisis 'Closing the Loop'")

# Simulasi nilai rata-rata kelas
st.write("#### Estimasi Ketercapaian CPL Mahasiswa:")
cpl_scores = pd.DataFrame({
    'CPL': ['CPL-S1', 'CPL-P1', 'CPL-P2', 'CPL-K1', 'CPL-K2'],
    'Target (%)': [80, 75, 75, 70, 70],
    'Realisasi (%)': [85, 72, 78, 65, 72]
})

st.table(cpl_scores)

for index, row in cpl_scores.iterrows():
    if row['Realisasi (%)'] < row['Target (%)']:
        st.error(f"⚠️ {row['CPL']} belum mencapai target. Rekomendasi: Perkuat intensitas praktikum/simulasi.")
    else:
        st.success(f"✅ {row['CPL']} telah melampaui target.")

# 5. Tombol Finalisasi
if st.button("Simpan Strategi OBLT/OBAE"):
    st.balloons()
    st.success("Strategi Pembelajaran dan Penilaian telah tersimpan dalam sistem!")
