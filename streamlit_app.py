import streamlit as st

# Konstanta Fisika
h = 6.62607015e-34   # Konstanta Planck (J·s)
c = 3e8              # Kecepatan cahaya (m/s)

st.title("🔮 Kalkulator Kuantum")
st.write("Hitung energi, frekuensi, dan panjang gelombang berdasarkan rumus kuantum Planck.")

# Pilihan Perhitungan
menu = st.selectbox(
    "Pilih jenis perhitungan:",
    ["Hitung Energi (E = h·f)", 
     "Hitung Frekuensi (f = E/h)", 
     "Hitung Panjang Gelombang dari Frekuensi (λ = c/f)",
     "Hitung Energi dari Panjang Gelombang (E = h·c/λ)"]
)

# ===============================
#       Perhitungan Energi
# ===============================

if menu == "Hitung Energi (E = h·f)":
    frekuensi = st.number_input("Masukkan frekuensi (Hz):", min_value=0.0)
    if st.button("Hitung Energi"):
        E = h * frekuensi
        st.success(f"Energi foton: {E} Joule")

# ===============================
#     Perhitungan Frekuensi
# ===============================

elif menu == "Hitung Frekuensi (f = E/h)":
    energi = st.number_input("Masukkan energi (Joule):", min_value=0.0)
    if st.button("Hitung Frekuensi"):
        f = energi / h
        st.success(f"Frekuensi: {f} Hz")

# ===========================================
#  Perhitungan Panjang Gelombang dari Frekuensi
# ===========================================

elif menu == "Hitung Panjang Gelombang dari Frekuensi (λ = c/f)":
    frekuensi = st.number_input("Masukkan frekuensi (Hz):", min_value=0.0)
    if st.button("Hitung Panjang Gelombang"):
        if frekuensi > 0:
            lam = c / frekuensi
            st.success(f"Panjang gelombang: {lam} meter")
        else:
            st.error("Frekuensi tidak boleh nol.")

# ===========================================
#   Perhitungan Energi dari Panjang Gelombang
# ===========================================

elif menu == "Hitung Energi dari Panjang Gelombang (E = h·c/λ)":
    lam = st.number_input("Masukkan panjang gelombang (meter):", min_value=0.0)
    if st.button("Hitung Energi"):
        if lam > 0:
            E = (h * c) / lam
            st.success(f"Energi foton: {E} Joule")
        else:
            st.error("Panjang gelombang tidak boleh nol.")
