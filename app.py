import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Judul Aplikasi
st.set_page_config(page_title="Estimasi Komposisi Kurikulum", layout="wide")
st.title("📊 Estimasi Komposisi Kurikulum (OBE)")
st.subheader("Berdasarkan Kepentingan Stakeholder")

# 2. Persiapan Data Stakeholder
stakeholders = [
    "Pengguna Lulusan", "Alumni", "Dosen Prodi", "Mahasiswa", 
    "Asosiasi Profesi", "Pemerintah", "Orang Tua", "Ahli Kurikulum", "Mitra"
]

# 3. Sidebar untuk Input Bobot Kepentingan (Tahap 1)
st.sidebar.header("1. Bobot Kepentingan (1-5)")
bobot_list = []
for s in stakeholders:
    b = st.sidebar.slider(f"Kepentingan {s}", 1, 5, 3)
    bobot_list.append(b)

# 4. Input Persepsi S-P-K (Tahap 2) - Menggunakan Table Editor
st.write("### 2. Masukkan Persepsi Unsur Kompetensi (0-100)")
st.write("Isi nilai Sikap, Pengetahuan, dan Keterampilan untuk tiap Stakeholder:")

default_data = {
    "Sikap": [90, 85, 80, 70, 85, 95, 90, 80, 75],
    "Pengetahuan": [70, 75, 90, 80, 85, 80, 70, 85, 80],
    "Keterampilan": [85, 80, 80, 90, 85, 75, 70, 85, 85]
}
df_input = pd.DataFrame(default_data, index=stakeholders)

# Fitur canggih Streamlit: Tabel yang bisa diedit langsung!
df_persepsi = st.data_editor(df_input)

# 5. Perhitungan Matematis (Tahap 3)
total_bobot = sum(bobot_list)
# Kalikan nilai dengan bobot masing-masing
df_tertimbang = df_persepsi.multiply(bobot_list, axis=0)
hasil_akhir = df_tertimbang.sum()
persentase = (hasil_akhir / hasil_akhir.sum()) * 100

# 6. Visualisasi Hasil
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.write("### 3. Estimasi Komposisi Akhir")
    for unsur, nilai in persentase.items():
        st.metric(label=unsur, value=f"{nilai:.2f} %")

with col2:
    # Grafik Pie Chart yang Cantik
    fig = px.pie(
        names=persentase.index, 
        values=persentase.values, 
        title="Proporsi Ideal Kurikulum",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig)

st.info("💡 Tip: Ubah nilai di tabel atau geser slider di kiri untuk melihat bagaimana komposisi kurikulum berubah secara otomatis!")
