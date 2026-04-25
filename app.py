import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Penyelarasan CPLEP - Unisba", layout="wide")
st.title("📊 Sistem Penyelarasan CPLEP")
st.subheader("Revisi Rumus Distribusi Kompetensi (Skala 1-4)")

# 2. Definisi Struktur
stakeholders = ["Mahasiswa", "PSEP", "Fakultas", "Universitas", "Yayasan", "LSP", "Bisnis", "Pemerintahan", "UCDC"]

sikap_cols = ["Integritas", "Kemandirian", "Kerjasama tim", "Komunikasi efektif", "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", "Kedisiplinan", "Keterbukaan", "Etika dan Moral"]
pengetahuan_cols = ["Kompetensi Inti Keilmuan", "Kompetensi Kuantitatif", "Kompetensi Kekhususan Dasar", "Kompetensi Keahlian", "Agama Islam"]
keterampilan_cols = ["Database", "Komputasi", "Presentasi", "Pengembangan Karir"]
all_cols = sikap_cols + pengetahuan_cols + keterampilan_cols

# 3. Sidebar: Bobot Stakeholder
st.sidebar.header("1. Bobot Stakeholder (1-5)")
bobot_list = []
for s in stakeholders:
    b = st.sidebar.slider(f"Bobot {s}", 1, 5, 3, key=f"slider_{s}")
    bobot_list.append(b)

# 4. Input Data (Skala 1-4)
st.write("### 2. Matriks Kepentingan Kompetensi")
if 'df_input' not in st.session_state:
    st.session_state.df_input = pd.DataFrame({col: [3] * len(stakeholders) for col in all_cols}, index=stakeholders)

# Gunakan on_change atau biarkan auto-update dari session_state
df_persepsi = st.data_editor(st.session_state.df_input, use_container_width=True, key="editor_final")

# 5. PERHITUNGAN LOGIKA (Gunakan .iloc agar aman dari KeyError)
list_S_rumus = ["Integritas", "Kemandirian", "Kerjasama tim", "Komunikasi efektif", "Keterbukaan", "Etika dan Moral"]
list_distribusi = ["Kerjasama tim", "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", "Kedisiplinan"]

# Hitung skor per baris
raw_S = df_persepsi[list_S_rumus].sum(axis=1)
raw_dist = df_persepsi[list_distribusi].sum(axis=1)
raw_P = df_persepsi[pengetahuan_cols].sum(axis=1)
raw_K = df_persepsi[keterampilan_cols].sum(axis=1)

# Terapkan rumus distribusi 0.6 & 0.4
skor_S_baris = raw_S
skor_P_baris = raw_P + (0.6 * raw_dist)
skor_K_baris = raw_K + (0.4 * raw_dist)

# Hitung Total Tertimbang (Looping yang aman)
weighted_S = 0
weighted_P = 0
weighted_K = 0

for i in range(len(stakeholders)):
    weighted_S += skor_S_baris.iloc[i] * bobot_list[i]
    weighted_P += skor_P_baris.iloc[i] * bobot_list[i]
    weighted_K += skor_K_baris.iloc[i] * bobot_list[i]

# Finalisasi ke Persentase
total_matriks = weighted_S + weighted_P + weighted_K
if total_matriks > 0:
    persentase = pd.Series({
        'Sikap': (weighted_S / total_matriks) * 100,
        'Pengetahuan': (weighted_P / total_matriks) * 100,
        'Keterampilan': (weighted_K / total_matriks) * 100
    })
else:
    persentase = pd.Series({'Sikap': 0, 'Pengetahuan': 0, 'Keterampilan': 0})

# 6. Visualisasi
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.write("### 3. Komposisi CPLEP Ideal")
    for k, v in persentase.items():
        st.metric(label=k, value=f"{v:.2f} %")
with c2:
    fig = px.pie(names=persentase.index, values=persentase.values, hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig)
