import streamlit as st

# --- Konfigurasi halaman ---
st.set_page_config(page_title="Persiapan Emosional Pra-Nikah", layout="centered")

# --- CSS untuk ubah warna latar belakang dan teks ---
st.markdown(
    """
    <style>
    /* Ubah warna latar belakang utama */
    .stApp {
        background-color: #000000;
        color: white;
    }

    /* Warna judul dan subjudul */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        text-align: center;
    }

    /* Atur warna teks biasa */
    p, div, span {
        color: #dddddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Persiapan Emosional Pra-Nikah")
st.subheader("AI dalam Psikologi Kelompok 1")

st.write("""
Selamat datang bla bla bla
""")

