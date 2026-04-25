import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi
st.set_page_config(page_title="Analisis Stakeholder SPK", page_icon="📊", layout="wide")
st.title("📊 Sistem Penyelarasan CPLEP")
st.subheader("Revisi Rumus Distribusi Kompetensi (Skala 1-4)")

# 2. Struktur Data
stakeholders = ["Mahasiswa", "PSEP", "Fakultas", "Universitas", "Yayasan", "LSP", "Bisnis", "Pemerintahan", "UCDC"]
sikap_cols = ["Integritas", "Kemandirian", "Kerjasama tim", "Komunikasi efektif", "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", "Kedisiplinan", "Keterbukaan", "Etika dan Moral"]
pengetahuan_cols = ["Kompetensi Inti Keilmuan", "Kompetensi Kuantitatif", "Kompetensi Kekhususan Dasar", "Kompetensi Keahlian", "Agama Islam"]
keterampilan_cols = ["Database", "Komputasi", "Presentasi", "Pengembangan Karir"]
all_cols = sikap_cols + pengetahuan_cols + keterampilan_cols

# 3. SIDEBAR - Bobot Stakeholder
st.sidebar.title("🧭 Navigasi Sistem")
st.sidebar.markdown("---")
# Kita buat dictionary untuk menampung nilai slider secara real-time
bobot_map = {}
for s in stakeholders:
    bobot_map[s] = st.sidebar.slider(f"Bobot {s}", 1, 5, 3, key=f"sl_{s}")

# 4. MATRIKS INPUT (Skala 1-4)
st.write("### 2. Matriks Kepentingan Kompetensi")

# Inisialisasi data jika belum ada
if 'df_data' not in st.session_state:
    st.session_state.df_data = pd.DataFrame({col: [3] * len(stakeholders) for col in all_cols}, index=stakeholders)

# Menampilkan tabel editor dan menyimpan hasilnya langsung ke session_state
df_persepsi = st.data_editor(st.session_state.df_data, use_container_width=True, key="editor_v3")

# 5. PERHITUNGAN (RUMUS REVISI)
# Mendefinisikan kelompok rumus
list_S_rumus = ["Integritas", "Kemandirian", "Kerjasama tim", "Komunikasi efektif", "Keterbukaan", "Etika dan Moral"]
list_distribusi = ["Kerjasama tim", "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", "Kedisiplinan"]

# Menghitung skor per baris (per stakeholder)
raw_S = df_persepsi[list_S_rumus].sum(axis=1)
raw_dist = df_persepsi[list_distribusi].sum(axis=1)
raw_P = df_persepsi[pengetahuan_cols].sum(axis=1)
raw_K = df_persepsi[keterampilan_cols].sum(axis=1)

# Rumus distribusi S, P, K
skor_S_baris = raw_S
skor_P_baris = raw_P + (0.6 * raw_dist)
skor_K_baris = raw_K + (0.4 * raw_dist)

# PENGALIAN DENGAN BOBOT SLIDER (Koneksi Inti)
weighted_S = 0
weighted_P = 0
weighted_K = 0

for s in stakeholders:
    # Mengalikan skor baris stakeholder 's' dengan bobot slider stakeholder 's'
    weighted_S += skor_S_baris.loc[s] * bobot_map[s]
    weighted_P += skor_P_baris.loc[s] * bobot_map[s]
    weighted_K += skor_K_baris.loc[s] * bobot_map[s]

# Finalisasi Persentase
total_SPK = weighted_S + weighted_P + weighted_K
if total_SPK > 0:
    persentase = pd.Series({
        'Sikap': (weighted_S / total_SPK) * 100,
        'Pengetahuan': (weighted_P / total_SPK) * 100,
        'Keterampilan': (weighted_K / total_SPK) * 100
    })
else:
    persentase = pd.Series({'Sikap': 0, 'Pengetahuan': 0, 'Keterampilan': 0})

# 6. VISUALISASI
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.write("### 3. Hasil Estimasi")
    for k, v in persentase.items():
        st.metric(label=k, value=f"{v:.2f} %")
    st.write(f"**Total Skor Tertimbang:** {total_SPK:.2f}")

with c2:
    fig = px.pie(names=persentase.index, values=persentase.values, hole=0.4, 
                 color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig)
