import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Profil Lulusan & CPL", layout="wide")
st.title("🎓 Tahap 2: Perumusan Profil & CPL")
st.subheader("Transformasi SPK menjadi Capaian Pembelajaran Lulusan")

# 2. Input Profil Lulusan
st.write("### A. Definisi Profil Lulusan")
col1, col2 = st.columns(2)

with col1:
    profil_1 = st.text_input("Profil Lulusan 1", "Analisis Kebijakan Ekonomi")
    desc_1 = st.text_area("Deskripsi Profil 1", "Mampu menganalisis fenomena ekonomi berbasis data dengan integritas tinggi.")

with col2:
    profil_2 = st.text_input("Profil Lulusan 2", "Entrepreneur Sektor Publik")
    desc_2 = st.text_area("Deskripsi Profil 2", "Mampu membangun inovasi ekonomi kreatif yang berdampak sosial.")

# 3. Referensi KKNI Level 6 (Internal Database)
st.divider()
st.write("### B. Penyelarasan KKNI Level 6 (Sarjana)")
with st.expander("Lihat Standar Kompetensi KKNI Level 6"):
    st.info("""
    1. Mampu mengaplikasikan bidang keahliannya dan memanfaatkan IPTEKS.
    2. Menguasai konsep teoritis bidang pengetahuan tertentu secara umum dan mendalam.
    3. Mampu mengambil keputusan yang tepat berdasarkan analisis informasi dan data.
    4. Bertanggung jawab pada pekerjaan sendiri dan dapat diberi tanggung jawab atas pencapaian hasil kerja organisasi.
    """)

# 4. Generator Butir CPL (Menggunakan KKO Bloom)
st.write("### C. Rumusan Capaian Pembelajaran Lulusan (CPL)")

# Fungsi sederhana untuk bantu narasi CPL
kko_kognitif = ["Menganalisis", "Mengevaluasi", "Mengonstruksi", "Memecahkan"]
kko_afektif = ["Menunjukkan", "Menginternalisasi", "Menghargai"]

# Membuat Tabel Input CPL
cpl_data = {
    "Kode": ["CPL-S1", "CPL-P1", "CPL-K1", "CPL-K2"],
    "Kategori": ["Sikap", "Pengetahuan", "Keterampilan", "Keterampilan"],
    "Kata Kerja (KKO)": [kko_afektif[1], kko_kognitif[0], kko_kognitif[2], "Mengoperasikan"],
    "Deskripsi Kompetensi": [
        "Nilai-nilai etika Islam dalam praktek ekonomi",
        "Teori ekonomi mikro dan makro secara mendalam",
        "Model ekonometri untuk prediksi pasar",
        "Sistem database dan komputasi statistik"
    ]
}

df_cpl = pd.DataFrame(cpl_data)

st.write("Edit butir CPL di bawah ini sesuai standar KKO:")
df_cpl_edited = st.data_editor(df_cpl, use_container_width=True, num_rows="dynamic")

# 5. Tombol Simpan & Ekspor
st.divider()
if st.button("Simpan & Finalisasi Kurikulum"):
    st.balloons()
    st.success("Data Profil dan CPL telah tersimpan ke dalam sistem!")
    
    # Simulasi Pratinjau Dokumen
    st.write("#### Pratinjau Matriks Kurikulum:")
    for index, row in df_cpl_edited.iterrows():
        st.write(f"**{row['Kode']}** ({row['Kategori']}): {row['Kata Kerja (KKO)']} {row['Deskripsi Kompetensi']}")

st.download_button(
    label="Unduh Naskah Akademik (Draft)",
    data=df_cpl_edited.to_csv().encode('utf-8'),
    file_name='Draft_Kurikulum_PSEP.csv',
    mime='text/csv',
)
