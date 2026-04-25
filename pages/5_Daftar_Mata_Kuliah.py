import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Struktur Mata Kuliah PSEP", page_icon="📑", layout="wide")
st.title("📑 Tahap 5: Struktur & Daftar Mata Kuliah")
st.markdown("---")

# 2. Input Mata Kuliah Baru (Berbasis Draft Revisi 6)
st.write("### A. Penyusunan Daftar Mata Kuliah")
st.info("Mata kuliah di bawah ini adalah hasil penurunan dari Bahan Kajian (PBK) yang telah disepakati.")

# Data draf mata kuliah awal
mk_data = {
    "Kode MK": ["EP101", "EP205", "EP302", "EP401", "EP405", "UNI102"],
    "Nama Mata Kuliah": [
        "Pengantar Ekonomi Digital", 
        "Ekonometrika & Dinamika Hamiltonian", 
        "Ekonomi Regional & Spasial", 
        "Circular Loop Economy",
        "Data Analytics untuk Ekonomi",
        "Etika Bisnis Islam (M3)"
    ],
    "SKS": [3, 4, 3, 3, 3, 2],
    "Semester": [1, 4, 5, 6, 7, 2],
    "Bahan Kajian Pendukung": [
        "Ekonomi Kontemporer & Digital",
        "Alat Analisis & Kuantitatif",
        "Ekonomi Sektoral & Wilayah",
        "Ekonomi Sektoral & Wilayah",
        "Ekonomi Kontemporer & Digital",
        "Nilai Islam & Karakter (M3)"
    ]
}

df_mk = pd.DataFrame(mk_data)

# Editor tabel untuk menambah/mengurangi MK
st.write("#### Edit atau Tambah Mata Kuliah:")
df_mk_edited = st.data_editor(df_mk, use_container_width=True, num_rows="dynamic")

# 3. Ringkasan Statistik Kurikulum
st.divider()
st.write("### B. Analisis Beban Kurikulum")
col1, col2, col3 = st.columns(3)

total_sks = df_mk_edited["SKS"].sum()
jumlah_mk = len(df_mk_edited)
rata_sks = df_mk_edited["SKS"].mean()

with col1:
    st.metric("Total SKS Terdaftar", f"{total_sks} SKS")
with col2:
    st.metric("Jumlah Mata Kuliah", f"{jumlah_mk} MK")
with col3:
    st.metric("Rata-rata SKS/MK", f"{rata_sks:.1f}")

# 4. Visualisasi Distribusi Semester
st.write("#### Distribusi Beban SKS per Semester:")
sks_per_sem = df_mk_edited.groupby("Semester")["SKS"].sum()
st.bar_chart(sks_per_sem)

# 5. Tombol Simpan & Download
st.divider()
if st.button("Finalisasi Struktur Kurikulum"):
    st.balloons()
    st.success(f"Selamat Kang Yuhka! Struktur Kurikulum PSEP dengan total {total_sks} SKS telah berhasil difinalisasi.")

st.download_button(
    label="📥 Unduh Daftar Mata Kuliah (Excel/CSV)",
    data=df_mk_edited.to_csv(index=False).encode('utf-8'),
    file_name='Struktur_Kurikulum_PSEP_2025.csv',
    mime='text/csv',
)
