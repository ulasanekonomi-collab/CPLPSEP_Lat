import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Profil & CPL PSEP 2025", page_icon="🎓", layout="wide")
st.title("🎓 Tahap 2: Profil Lulusan & CPL (Revisi 2025)")
st.markdown("---")

# 2. Input Profil Lulusan Berbasis Karakter Unisba
st.write("### A. Profil Lulusan (Mujahid, Mujtahid, Mujaddid)")
st.info("Profil ini mengacu pada draf revisi kurikulum terbaru yang menekankan integrasi nilai Islam dan daya saing digital.")

col1, col2 = st.columns(2)

with col1:
    profil_1 = st.text_input("Profil 1: Data-Driven Analyst (Mujtahid)", "Analis Ekonomi Digital")
    desc_1 = st.text_area("Deskripsi Profil 1", 
                         "Tenaga ahli yang tekun dalam mengolah data besar (Big Data) untuk menghasilkan rekomendasi kebijakan ekonomi yang presisi.")

    profil_2 = st.text_input("Profil 2: Policy Planner (Mujaddid)", "Perencana Pembangunan Inovatif")
    desc_2 = st.text_area("Deskripsi Profil 2", 
                         "Pebaharu yang mampu merancang strategi pembangunan wilayah dengan pendekatan sustainable dan circular economy.")

with col2:
    profil_3 = st.text_input("Profil 3: Social Impact Manager (Mujahid)", "Manajer Pemberdayaan Sosial")
    desc_3 = st.text_area("Deskripsi Profil 3", 
                         "Pejuang ekonomi yang tangguh dalam mengelola program pemberdayaan masyarakat berbasis nilai-nilai keislaman.")

    profil_4 = st.text_input("Profil 4: Value-Based Professional", "Ekonom Beretika Islam")
    desc_4 = st.text_area("Deskripsi Profil 4", 
                         "Profesional yang mengintegrasikan hukum syariah dan etika moral dalam setiap pengambilan keputusan finansial.")

# 3. Sinkronisasi CPL dengan KKO "Ganas" (Level 6 KKNI)
st.divider()
st.write("### B. Matriks Capaian Pembelajaran Lulusan (CPL)")
st.caption("Gunakan Kata Kerja Operasional (KKO) tinggi: Menganalisis, Mengevaluasi, Mengonstruksi.")

# Data CPL Berdasarkan Draft Revisi 6
cpl_data = {
    "Kode": ["CPL-S1", "CPL-P1", "CPL-P2", "CPL-K1", "CPL-K2", "CPL-K3"],
    "Kategori": ["Sikap", "Pengetahuan", "Pengetahuan", "Keterampilan", "Keterampilan", "Keterampilan"],
    "KKO Utama": ["Menginternalisasi", "Mengevaluasi", "Menganalisis", "Mengonstruksi", "Mengoperasikan", "Memecahkan"],
    "Deskripsi Kompetensi": [
        "Nilai-nilai Mujahid, Mujtahid, dan Mujaddid dalam profesi ekonomi.",
        "Teori ekonomi makro-mikro dan kebijakan fiskal-moneter kontemporer.",
        "Konsep ekonomi digital, green economy, dan circular loop integration.",
        "Model ekonometrika dan simulasi sistem dinamis (Hamiltonian).",
        "Perangkat lunak analisis data (Python, R, atau STATA) dan AI.",
        "Masalah pembangunan wilayah melalui pendekatan spasial dan sosial."
    ]
}

df_cpl = pd.DataFrame(cpl_data)
df_cpl_edited = st.data_editor(df_cpl, use_container_width=True, num_rows="dynamic")

# 4. Fitur Baru: Cek Keselarasan (Self-Audit)
st.divider()
st.write("### C. Audit Keselarasan Kurikulum")
total_kko_tinggi = df_cpl_edited[df_cpl_edited['KKO Utama'].isin(['Mengevaluasi', 'Menganalisis', 'Mengonstruksi', 'Memecahkan'])].shape[0]

if total_kko_tinggi >= 3:
    st.success(f"✅ Bagus! Terdapat {total_kko_tinggi} CPL dengan standar KKO tinggi. Kurikulum memenuhi syarat KKNI Level 6.")
else:
    st.warning("⚠️ Perhatian: Tambahkan lebih banyak KKO level tinggi (Analisis/Evaluasi) untuk memenuhi standar Sarjana.")

# 5. Tombol Ekspor
if st.button("Simpan & Generate Naskah Akademik"):
    st.balloons()
    st.success("Naskah Akademik berhasil diperbarui!")
    
    # Pratinjau Output
    st.markdown("---")
    st.write("#### Ringkasan Dokumen Kurikulum PSEP 2025")
    st.write(f"**Visi Profil:** {profil_1}, {profil_2}, {profil_3}")
    st.table(df_cpl_edited[['Kode', 'KKO Utama', 'Deskripsi Kompetensi']])

st.download_button(
    label="📥 Unduh Draft Struktur CPL (Excel/CSV)",
    data=df_cpl_edited.to_csv(index=False).encode('utf-8'),
    file_name='CPL_PSEP_2025_Revisi6.csv',
    mime='text/csv',
)
