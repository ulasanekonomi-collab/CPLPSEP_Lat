import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Konfigurasi Halaman agar terlihat Luas & Modern
st.set_page_config(page_title="Dashboard Analisis CPL", layout="wide", page_icon="📈")

st.title("📊 Dashboard Komputasi Estimasi Kurikulum (CPL)")
st.markdown("""
Sistem ini mengestimasi komposisi ideal kurikulum berdasarkan **Weighted Stakeholder Analysis**. 
Silakan atur bobot kepentingan di samping dan detail persepsi di tabel bawah.
""")

# 2. Inisialisasi Data Stakeholder
stakeholders = [
    "Pengguna Lulusan", "Alumni", "Dosen Prodi", "Mahasiswa Aktif", 
    "Asosiasi Profesi", "Pemerintah (Dikti)", "Orang Tua", "Ahli Kurikulum", "Mitra Strategis"
]

# 3. Sidebar: Pengaturan Bobot Kepentingan
st.sidebar.header("🎯 Bobot Kepentingan")
st.sidebar.info("Skala 1 (Rendah) s/d 5 (Kritis)")
bobot_list = []
for s in stakeholders:
    b = st.sidebar.select_slider(f"{s}", options=[1, 2, 3, 4, 5], value=3, key=s)
    bobot_list.append(b)

# 4. Main Area: Editor Data Persepsi
st.subheader("📝 Matriks Persepsi Stakeholder")
default_data = {
    "Sikap": [90, 85, 80, 70, 85, 95, 90, 80, 75],
    "Pengetahuan": [70, 75, 90, 80, 85, 80, 70, 85, 80],
    "Keterampilan": [85, 80, 80, 90, 85, 75, 70, 85, 85]
}
df_input = pd.DataFrame(default_data, index=stakeholders)

# Tabel interaktif
df_persepsi = st.data_editor(df_input, use_container_width=True)

# 5. Mesin Komputasi (The Logic)
df_tertimbang = df_persepsi.multiply(bobot_list, axis=0)
hasil_akhir = df_tertimbang.sum()
persentase = (hasil_akhir / hasil_akhir.sum()) * 100

# 6. Baris Hasil (Metrik & Grafik)
st.divider()
col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    st.write("### 💎 Skor Akhir")
    for unsur, nilai in persentase.items():
        st.metric(label=unsur, value=f"{nilai:.2f}%")

with col2:
    # Grafik Pie
    fig_pie = px.pie(
        names=persentase.index, 
        values=persentase.values, 
        hole=0.4,
        title="Komposisi Proporsional",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col3:
    # Grafik Batang untuk perbandingan tegas
    fig_bar = px.bar(
        x=persentase.index, 
        y=persentase.values,
        title="Distribusi Kompetensi",
        labels={'x': 'Unsur', 'y': 'Persentase (%)'},
        color=persentase.index,
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# 7. Narasi Kesimpulan Otomatis
st.divider()
st.write("### 📋 Kesimpulan Strategis")
unsur_tertinggi = persentase.idxmax()
st.success(f"Berdasarkan analisis, kurikulum ini harus memberikan penekanan utama pada unsur **{unsur_tertinggi}** ({persentase.max():.2f}%).")

# Tombol Download Data
csv = df_persepsi.to_csv().encode('utf-8')
st.download_button(
    label="📥 Download Data Matriks (CSV)",
    data=csv,
    file_name='matriks_stakeholder_cpl.csv',
    mime='text/csv',
)
