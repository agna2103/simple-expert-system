import streamlit as st

st.set_page_config(page_title="Persiapan Emosional Pra-Nikah", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #2E003E;
        color: white;
    }
    .banner-img {
        position: fixed;
        top: 15px;
        right: 25px;
        width: 100px;
        border-radius: 8px;
        box-shadow: 0px 0px 6px rgba(0,0,0,0.5);
        z-index: 9999;
    }
    </style>

    <img src="https://github.com/agna2103/simple-expert-system/blob/9aff16990de6ec130049b18a2e502c469492b66c/download.webp?raw=true" class="banner-img">
    """,
    unsafe_allow_html=True
)

st.title("Persiapan Emosional Pra-Nikah")
st.subheader("AI dalam Psikologi Kelompok 1")
st.write("Selamat datang di aplikasi ini! 💜")
