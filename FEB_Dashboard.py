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
# --- BAGIAN BARU: INSTRUMEN STRESS TEST BERBASIS DOKUMEN ---
st.divider()
st.write("### 🧪 Instrumen Stress Test (Vertical Alignment Analysis)")
st.info("Gunakan instrumen ini untuk memastikan Visi tidak berhenti di level normatif, tapi teroperasionalkan dalam sistem kurikulum.")

# Pertanyaan kunci berdasarkan metode Stress Test Akang
pertanyaan_audit = [
    "Visi → CPL: Apakah elemen utama visi (Kemaslahatan & Society 5.0) telah diterjemahkan secara eksplisit dalam CPL?",
    "CPL → Mata Kuliah: Apakah struktur mata kuliah telah merepresentasikan CPL secara proporsional?",
    "Mata Kuliah → OBLT: Apakah aktivitas pembelajaran secara nyata melatih kompetensi yang sesuai dengan visi?",
    "Pembelajaran → OBAE: Apakah capaian terkait visi dapat diukur secara objektif dan berbasis bukti?"
]

with st.expander("📝 Form Audit Kesesuaian Kurikulum"):
    skor_audit = []
    for i, tanya in enumerate(pertanyaan_audit):
        st.write(f"**{tanya}**")
        skor = st.select_slider(f"Penilaian Q{i+1}:", 
                               options=["Sangat Lemah", "Lemah", "Cukup", "Kuat", "Sangat Kuat"], 
                               key=f"st_audit_{i}")
        skor_audit.append(skor)
    
    st.divider()
    st.write("#### 🔍 Analisis Kesenjangan (Gap Analysis)")
    catatan_gap = st.text_area("Masukkan temuan kesenjangan antara desain normatif dan implementasi operasional:", 
                               placeholder="Contoh: Integrasi nilai kemaslahatan masih cenderung terpisah dalam mata kuliah tertentu...")

# Tombol Eksekusi Analisis
if st.button("Jalankan Uji Kesesuaian"):
    st.subheader("🏁 Kesimpulan Stress Test")
    
    # Menampilkan hasil berdasarkan prinsip dokumen Akang
    if "Sangat Lemah" in skor_audit or "Lemah" in skor_audit:
        st.error("🚨 HASIL: Visi belum sepenuhnya terinternalisasi secara operasional.")
        st.write("**Rekomendasi Langkah Lanjutan:**")
        st.markdown("""
        - **Refinement CPL:** Penajaman rumusan agar lebih operasional dan terukur[cite: 33].
        - **Integrasi Mata Kuliah:** Menanamkan nilai kemaslahatan dalam mata kuliah inti ekonomi[cite: 25].
        - **Penguatan OBAE:** Pengembangan instrumen asesmen untuk dimensi nilai dan teknologi[cite: 27].
        """)
    else:
        st.success("✅ HASIL: Kurikulum telah memiliki landasan kuat secara filosofis dan operasional[cite: 23].")
    
    st.balloons()
