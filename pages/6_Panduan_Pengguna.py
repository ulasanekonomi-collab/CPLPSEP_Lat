import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Panduan Dashboard PSEP", page_icon="📖", layout="wide")
st.title("📖 Panduan Penggunaan Dashboard Kurikulum")
st.markdown("---")

st.write("### Selamat Datang, Tim Kurikulum PSEP!")
st.write("Dashboard ini dirancang untuk memudahkan penyelarasan kurikulum berbasis **Outcome-Based Education (OBE)** sesuai draf revisi 2025.")

# 2. Alur Kerja (Timeline)
st.info("#### 💡 Alur Kerja 5 Tahap:")

with st.expander("🔍 Tahap 1: Analisis Stakeholder (Halaman Utama)"):
    st.write("""
    - **Tujuan:** Menangkap preferensi kompetensi dari alumni, bisnis, dan pakar.
    - **Cara:** Gunakan slider untuk menentukan bobot Sikap, Pengetahuan, dan Keterampilan. 
    - **Hasil:** Grafik radar akan menunjukkan arah pengembangan kurikulum.
    """)

with st.expander("🎓 Tahap 2: Profil & CPL"):
    st.write("""
    - **Tujuan:** Menentukan identitas lulusan (Mujahid, Mujtahid, Mujaddid).
    - **Cara:** Masukkan narasi profil dan butir CPL. 
    - **Fitur Khusus:** Terdapat audit otomatis untuk memastikan penggunaan Kata Kerja Operasional (KKO) tinggi sesuai KKNI Level 6.
    """)

with st.expander("🚀 Tahap 3: Simulator MBKM"):
    st.write("""
    - **Tujuan:** Memberikan gambaran fleksibilitas karir mahasiswa.
    - **Cara:** Pilih paket minat (Digital Economy, Regional, dll).
    - **Hasil:** Lihat mata kuliah prodi mitra yang dikonversi dan dampaknya pada penguatan CPL.
    """)

with st.expander("📚 Tahap 4: Pemetaan Bahan Kajian (PBK)"):
    st.write("""
    - **Tujuan:** Menentukan 'menu' ilmu pengetahuan.
    - **Cara:** Petakan butir CPL ke Kelompok Bahan Kajian (seperti Alat Analisis/Hamiltonian).
    """)

with st.expander("📑 Tahap 5: Struktur Mata Kuliah"):
    st.write("""
    - **Tujuan:** Finalisasi draf kurikulum.
    - **Cara:** Masukkan nama MK, SKS, dan Semester.
    - **Fitur Khusus:** Sistem menghitung total SKS otomatis dan menyediakan tombol download Excel.
    """)

# 3. Kontak & Dukungan
st.divider()
st.warning("⚠️ **Catatan:** Jangan lupa untuk mengunduh (Download) hasil draf dari Halaman 5 sebelum menutup browser agar data tetap tersimpan dalam format file.")

st.markdown("""
**Penyusun Sistem:** Kang Yuhka Sundaya  
**Versi:** 1.0 (Draft 6 - 2025)  
**Institusi:** Ekonomi Pembangunan - Unisba
""")
