import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Judul Aplikasi
st.set_page_config(page_title="Penyelarasan CPLEP - Unisba", layout="wide")
st.title("📊 Sistem Penyelarasan CPLEP")
st.subheader("Estimasi Komposisi Kurikulum Berdasarkan Kepentingan Stakeholder")

# 2. Definisi Struktur Stakeholder & Kolom
stakeholders = [
    "Mahasiswa", "PSEP", "Fakultas", "Universitas", "Yayasan", 
    "LSP", "Bisnis", "Pemerintahan", "UCDC"
]

# Definisi Sub-Unsur
sikap_cols = [
    "Integritas", "Kemandirian", "Kerjasama tim", "Komunikasi efektif", 
    "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", 
    "Kedisiplinan", "Keterbukaan", "Etika dan Moral"
]
pengetahuan_cols = [
    "Kompetensi Inti Keilmuan", "Kompetensi Kuantitatif", 
    "Kompetensi Kekhususan Dasar", "Kompetensi Keahlian", "Agama Islam"
]
keterampilan_cols = [
    "Database", "Komputasi", "Presentasi", "Pengembangan Karir"
]

all_cols = sikap_cols + pengetahuan_cols + keterampilan_cols

# 3. Sidebar: Bobot Kepentingan Stakeholder
st.sidebar.header("1. Tingkat Kepentingan (1-5)")
bobot_list = []
for s in stakeholders:
    b = st.sidebar.slider(f"Bobot {s}", 1, 5, 3)
    bobot_list.append(b)

# 4. Input Data Persepsi
st.write("### 2. Matriks Persepsi Stakeholder")
st.caption("Isi nilai (0-100) untuk setiap sub-unsur di bawah ini:")

# Membuat template data awal (default 80 agar tidak kosong)
default_data = {col: [80] * len(stakeholders) for col in all_cols}
df_input = pd.DataFrame(default_data, index=stakeholders)

# Editor Tabel yang bisa digeser/edit
df_persepsi = st.data_editor(df_input, use_container_width=True)

# 5. Perhitungan Logika CPLEP
# a. Hitung rata-rata per kategori (S, P, K) untuk tiap stakeholder
df_persepsi['Sikap_Avg'] = df_persepsi[sikap_cols].mean(axis=1)
df_persepsi['Pengetahuan_Avg'] = df_persepsi[pengetahuan_cols].mean(axis=1)
df_persepsi['Keterampilan_Avg'] = df_persepsi[keterampilan_cols].mean(axis=1)

# b. Kalikan dengan Bobot Kepentingan
df_weighted = pd.DataFrame(index=stakeholders)
df_weighted['Sikap'] = df_persepsi['Sikap_Avg'] * bobot_list
df_weighted['Pengetahuan'] = df_persepsi['Pengetahuan_Avg'] * bobot_list
df_weighted['Keterampilan'] = df_persepsi['Keterampilan_Avg'] * bobot_list

# c. Hasil Akhir
total_skor = df_weighted.sum()
persentase = (total_skor / total_skor.sum()) * 100

# 6. Visualisasi & Laporan
st.divider()
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 3. Estimasi Komposisi Ideal")
    for unsur, nilai in persentase.items():
        st.metric(label=f"Porsi {unsur}", value=f"{nilai:.2f} %")
    
    st.write("#### Detail Rata-rata per Kategori:")
    st.dataframe(df_persepsi[['Sikap_Avg', 'Pengetahuan_Avg', 'Keterampilan_Avg']].style.highlight_max(axis=1))

with col2:
    fig = px.pie(
        names=persentase.index, 
        values=persentase.values, 
        title="Persentase S-P-K Akhir",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig)

st.success("✅ Analisis Selesai: Gunakan hasil ini sebagai dasar penentuan bobot SKS atau distribusi mata kuliah.")
