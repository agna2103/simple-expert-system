import streamlit as st


# --- Konfigurasi halaman ---
st.set_page_config(page_title="Persiapan Emosional Pra-Nikah", layout="centered")

# --- Gaya kustom (CSS) ---
st.markdown(
    """
    <style>
    /* ====== LATAR BELAKANG ====== */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/agna2103/simple-expert-system/main/pexels-rocsana99-948185.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        position: relative;
    }

    /* ====== OVERLAY UNGU TRANSPARAN ====== */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(128, 0, 128, 0.6); /* Warna ungu dengan transparansi 60% */
        z-index: 0;
    }

    /* ====== KONTEN UTAMA ====== */
    .block-container {
        position: relative;
        z-index: 1;
        color: white;
        text-align: center;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
    }

    p, div, span {
        color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Konten utama ---
st.title("Persiapan Emosional Pra-Nikah")
st.subheader("AI dalam Psikologi Kelompok 1")

st.write("""
Selamat datang di aplikasi ini! 🌿  
Di sini kita akan membahas pentingnya **persiapan emosional sebelum pernikahan**,  
dengan bantuan **AI dalam bidang psikologi**.
""")


