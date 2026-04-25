import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FEB Unisba Command Center", page_icon="🏢", layout="wide")
st.title("🏢 FEB Unisba Curriculum Command Center")
st.subheader("Instrumen Koordinasi & Supervisi Kurikulum Fakultas")
st.markdown("---")

# Ringkasan Kesiapan
st.write("### 📊 Status Kesiapan Kurikulum OBE")
col1, col2, col3 = st.columns(3)
col1.metric("Prodi EP", "95%", "Revisi 6")
col2.metric("Prodi Manajemen", "70%", "Perlu Review")
col3.metric("Prodi Akuntansi", "85%", "Finalisasi")

# Grafik KKO (High Order Thinking)
st.divider()
st.write("### 🛡️ Dashboard Otoritas Fakultas")
data_kko = pd.DataFrame({
    'Prodi': ['EP', 'Manajemen', 'Akuntansi'],
    'KKO Tinggi (C4-C6)': [78, 45, 60],
    'KKO Menengah (C1-C3)': [22, 55, 40]
})
fig = px.bar(data_kko, x='Prodi', y=['KKO Tinggi (C4-C6)', 'KKO Menengah (C1-C3)'], barmode='group')
st.plotly_chart(fig, use_container_width=True)

# Panel Persetujuan Dekan
st.divider()
prodi = st.selectbox("Review Prodi:", ["Ekonomi Pembangunan", "Manajemen", "Akuntansi"])
st.text_area(f"Catatan Dekan untuk {prodi}:", "Dokumen sesuai standar OBE.")
if st.button("Kirim Validasi Fakultas"):
    st.balloons()
    st.success("Rekomendasi Terkirim!")
# --- UPDATE: INSTRUMEN STRESS TEST DENGAN PARAMETER OBJEKTIF ---
st.divider()
st.write("### 🧪 Instrumen Stress Test (Vertical Alignment Analysis)")
st.info("Parameter ini membantu pimpinan menilai apakah Visi sudah turun ke level operasional atau masih di level normatif.")

# Definisi Parameter berdasarkan dokumen Akang
audit_params = {
    "Visi → CPL": {
        "tanya": "Apakah elemen 'Kemaslahatan' & 'Society 5.0' sudah muncul eksplisit di CPL?",
        "parameter": "Sangat Kuat jika: Muncul di semua ranah (Sikap, Pengetahuan, Keterampilan) secara spesifik."
    },
    "CPL → Mata Kuliah": {
        "tanya": "Apakah struktur Mata Kuliah sudah merepresentasikan CPL secara proporsional?",
        "parameter": "Sangat Kuat jika: Mata kuliah inti (bukan hanya MK Agama/Pilihan) memuat konten Visi."
    },
    "MK → OBLT": {
        "tanya": "Apakah metode pembelajaran secara nyata melatih kompetensi Visi?",
        "parameter": "Sangat Kuat jika: Menggunakan Case-Based atau Project-Based dengan data riil digital."
    },
    "OBLT → OBAE": {
        "tanya": "Apakah capaian Visi dapat diukur secara objektif berbasis bukti?",
        "parameter": "Sangat Kuat jika: Memiliki Rubrik Penilaian yang mengukur aspek nilai dan teknologi secara terukur."
    }
}

with st.expander("📝 Form Audit dengan Parameter"):
    skor_audit = []
    for key, val in audit_params.items():
        st.write(f"**{key}**")
        st.markdown(f"*{val['tanya']}*")
        st.caption(f"📍 **Parameter:** {val['parameter']}") # Ini parameternya, Kang!
        
        skor = st.select_slider(f"Skor {key}:", 
                               options=["Lemah", "Cukup", "Kuat", "Sangat Kuat"], 
                               key=f"audit_v2_{key}")
        skor_audit.append(skor)
        st.write("---")
    
    catatan_gap = st.text_area("Gap Analysis (Temuan Kesenjangan):", 
                               placeholder="Tuliskan di sini jika parameter di atas belum terpenuhi...")

# Tombol Analisis
if st.button("Jalankan Audit Kesesuaian"):
    st.subheader("🏁 Hasil Kesimpulan Stress Test")
    
    # Logika evaluasi
    if "Sangat Kuat" in skor_audit and "Lemah" not in skor_audit:
        st.success("✅ KURIKULUM MATANG: Visi telah teroperasionalkan dengan baik hingga level asesmen.")
    else:
        st.warning("⚠️ KURIKULUM KONTEKSTUAL: Visi masih dominan di level normatif/konsep. Perlu penajaman di level OBLT & OBAE.")
    
    st.balloons()
