import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Simulasi MBKM PSEP", page_icon="🚀", layout="wide")
st.title("🚀 Tahap 3: Simulator Paket MBKM")
st.markdown("---")

# 2. Database Paket MBKM (Berdasarkan Draft Revisi 6 Akang)
paket_mbkm = {
    "Paket 4: Digital Economy & Finance": {
        "Prodi Asal": "Manajemen / Akuntansi",
        "Mata Kuliah": ["Fintech", "Analisis Laporan Keuangan", "Manajemen Investasi"],
        "Konversi": "Manajemen Keuangan & Analisis Investasi",
        "CPL Utama": "Keterampilan Khusus (K2)",
        "Rasional": "Memberikan landasan kuat dalam pengambilan keputusan finansial dan investasi digital."
    },
    "Paket 5: Regional & Spatial Development": {
        "Prodi Asal": "PWK / Geografi",
        "Mata Kuliah": ["Perencanaan Wilayah", "Analisis Tata Ruang", "Sistem Informasi Geografis"],
        "Konversi": "Ekonomi Regional & Spasial",
        "CPL Utama": "Keterampilan Khusus (K3)",
        "Rasional": "Mendukung analisis pembangunan berbasis wilayah yang menjadi core kompetensi ekonomi pembangunan."
    },
    "Paket 6: Behavioral & Social Analysis": {
        "Prodi Asal": "Psikologi / Sosiologi",
        "Mata Kuliah": ["Psikologi Sosial", "Psikologi Konsumen", "Sosiologi Ekonomi"],
        "Konversi": "Behavioral Economics",
        "CPL Utama": "Sikap (S1) & Pengetahuan (P2)",
        "Rasional": "Memperkaya analisis ekonomi dengan pendekatan perilaku dan sosial masyarakat."
    }
}

# 3. Sidebar Navigasi Simulasi
st.sidebar.header("🎯 Pilih Minat Karir")
minat = st.sidebar.selectbox("Saya ingin fokus sebagai:", 
                            ["Data-Driven Analyst", "Regional Planner", "Financial Specialist", "Social Consultant"])

# 4. Area Simulasi
st.write(f"### Simulasi Rekomendasi untuk: **{minat}**")

col1, col2 = st.columns([1, 2])

with col1:
    st.write("#### 🛠 Pilih Paket MBKM:")
    pilihan_paket = st.radio("Daftar Paket Tersedia:", list(paket_mbkm.keys()))
    
    st.divider()
    if st.button("Ambil Paket Ini!"):
        st.balloons()
        st.success(f"Berhasil! Paket ini akan dikonversi menjadi mata kuliah: **{paket_mbkm[pilihan_paket]['Konversi']}**")

with col2:
    st.write("#### 📝 Detail Kompetensi Paket:")
    detail = paket_mbkm[pilihan_paket]
    
    st.markdown(f"""
    * **Prodi Mitra:** {detail['Prodi Asal']}
    * **Mata Kuliah Diambil:** {', '.join(detail['Mata Kuliah'])}
    * **Mendukung CPL:** `{detail['CPL Utama']}`
    * **Rasionalitas:** {detail['Rasional']}
    """)
    
    # Visualisasi Dampak CPL (Dummy Data)
    st.write("#### 📈 Estimasi Penguatan Kompetensi:")
    chart_data = pd.DataFrame({
        'Aspek': ['Sikap', 'Pengetahuan', 'Keterampilan'],
        'Peningkatan (%)': [15 if "S1" in detail['CPL Utama'] else 5, 
                            20 if "P" in detail['CPL Utama'] else 10, 
                            25 if "K" in detail['CPL Utama'] else 10]
    })
    fig = px.bar(chart_data, x='Aspek', y='Peningkatan (%)', color='Aspek', 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

# 5. Footer Dokumen
st.divider()
st.caption("PSEP Equilibrium Dashboard - Modul MBKM Berbasis Draft Revisi 6 (2025)")
