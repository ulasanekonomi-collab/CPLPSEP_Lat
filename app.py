# 5. PERHITUNGAN DENGAN RUMUS REVISI (Cross-Cutting Competency)

# a. Mendefinisikan kelompok sesuai simbol S1-S10, P1-P5, K1-K4
# Sikap yang murni masuk ke S
S_murni = ["Integritas", "Kemandirian", "Keterbukaan", "Etika dan Moral"] # S1, S2, S9, S10
# Sikap yang didistribusikan (S3, S5, S6, S7, S8)
S_distribusi = ["Kerjasama tim", "Kreatif dan inovatif", "Tanggung jawab", "Empati dan peduli", "Kedisiplinan"] 
# Tambahkan S4 (Komunikasi Efektif) ke S_murni sesuai list Akang (S1, S2, S3, S4, S9, S10)
# Tapi tunggu, di rumus Akang S3 masuk ke S, P, dan K. Mari kita ikuti persis rumus Akang:

# b. Hitung Total per baris (per stakeholder)
total_S_rumus = df_persepsi["Integritas"] + df_persepsi["Kemandirian"] + df_persepsi["Kerjasama tim"] + \
                df_persepsi["Komunikasi efektif"] + df_persepsi["Keterbukaan"] + df_persepsi["Etika dan Moral"]

S_dist_total = df_persepsi["Kerjasama tim"] + df_persepsi["Kreatif dan inovatif"] + \
               df_persepsi["Tanggung jawab"] + df_persepsi["Empati dan peduli"] + df_persepsi["Kedisiplinan"]

total_P_murni = df_persepsi[pengetahuan_cols].sum(axis=1)
total_K_murni = df_persepsi[keterampilan_cols].sum(axis=1)

# c. Terapkan Rumus Bobot (P + 0.6*dist dan K + 0.4*dist)
skor_S = total_S_rumus
skor_P = total_P_murni + (0.6 * S_dist_total)
skor_K = total_K_murni + (0.4 * S_dist_total)

# d. Kalikan dengan Bobot Kepentingan Stakeholder (bobot_list dari sidebar)
weighted_S = (skor_S * bobot_list).sum()
weighted_P = (skor_P * bobot_list).sum()
weighted_K = (skor_K * bobot_list).sum()

# e. Normalisasi ke Persentase (Total Matriks)
total_matriks = weighted_S + weighted_P + weighted_K
persentase = pd.Series({
    'Sikap': (weighted_S / total_matriks) * 100,
    'Pengetahuan': (weighted_P / total_matriks) * 100,
    'Keterampilan': (weighted_K / total_matriks) * 100
})
