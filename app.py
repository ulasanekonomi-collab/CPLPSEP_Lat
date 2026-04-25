import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Judul Aplikasi
st.set_page_config(page_title="Penyelarasan CPLEP - Unisba", layout="wide")
st.title("📊 Sistem Penyelarasan CPLEP")
st.subheader("Revisi Rumus Distribusi Kompetensi (Skala 1-4)")

# 2. Definisi Struktur Stakeholder & Kolom
stakeholders = [
    "Mahasiswa", "PSEP", "Fakultas", "Universitas", "Yayasan", 
    "LSP", "Bisnis", "Pemerintahan", "UCDC"
]

# Daftar Sub-Unsur S, P, K
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

# 3. Sidebar: Bobot Kepentingan Stakeholder (Skala 1-5 untuk Kepentingan Stakeholder)
st.sidebar.header("1. Bobot Stakeholder (1-5)")
bobot_list = []
for s in stakeholders:
    b = st.sidebar.slider(f"Bobot {s}", 1, 5, 3)
    bobot_list.append(b)

# 4. Input Data Persepsi (Skala 1-4)
st.write("### 2. Matriks Kepentingan Kompetensi")
st.info("Silakan isi dengan skala 1-4 (1: Tidak Penting, 4: Sangat Penting)")

# Template data awal (Default skala 3)
if 'df_awal' not in st.session_state:
    default_data = {col: [3] * len(stakeholders) for col in all_cols}
    st.session_state.df_awal = pd.DataFrame(default_data, index=stakeholders)

# Editor Tabel
df_persepsi = st.data_editor(st.session_state.df_awal, use_container_width=True)

# 5. PERHITUNGAN SESUAI RUMUS REVISI
# List sesuai pengelompokan rumus Kang Yuhka
list_S_rumus = ["Integritas", "Kemandirian", "Kerjasama tim", "Komunikasi efektif", "Keterbukaan", "Etika dan Moral"]
list_distribusi = ["Kerjasama tim", "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", "Kedisiplinan"]

# a. Hitung total mentah per baris (per stakeholder)
raw_S = df_persepsi[list_S_rumus].sum(axis=1)
raw_dist = df_persepsi[list_distribusi].sum(axis=1)
raw_P = df_persepsi[pengetahuan_cols].sum(axis=1)
raw_K = df_persepsi[keterampilan_cols].sum(axis=1)

# b. Terapkan Bobot Distribusi
# S = (S1+S2+S3+S4+S9+S10)
# P = Total P + 0.6*(S3+S5+S6+S7+S8)
# K = Total K + 0.4*(S3+S5+S6+S7+S8)
skor_S_baris = raw_S
skor_P_baris = raw_P + (0.6 * raw_dist)
skor_K_baris = raw_K + (0.4 * raw_dist)

# c. Kalikan dengan Bobot Stakeholder
weighted_S = (skor_S_baris * bobot_list).sum()
weighted_P = (skor_P_baris * bobot_list).sum()
weighted_K = (skor_K_baris * bobot_list).sum()

# d. Finalisasi Persentase (Dibagi Total Matriks)
total_matriks = weighted_S + weighted_P + weighted_K
persentase = pd.Series({
    'Sikap': (weighted_S / total_matriks) * 100,
    'Pengetahuan': (weighted_P / total_matriks) * 100,
    'Keterampilan': (weighted_K / total_matriks) * 100
})

# 6. Visualisasi
st.divider()
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 3. Komposisi CPLEP Ideal")
    for unsur, nilai in persentase.items():
        st.metric(label=unsur, value=f"{nilai:.2f} %")
    
    st.write("#### Ringkasan Skor Tertimbang:")
    st.write(f"- Sikap: **{weighted_S:.2f}**")
    st.write(f"- Pengetahuan: **{weighted_P:.2f}**")
    st.write(f"- Keterampilan: **{weighted_K:.2f}**")

with col2:
    fig = px.pie(
        names=persentase.index, 
        values=persentase.values, 
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig)

st.success("Analisis berhasil diperbarui sesuai rumus distribusi bobot 0.6 & 0.4.")
