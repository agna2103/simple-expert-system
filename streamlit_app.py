import streamlit as st


st.markdown(
    """ 
    <style>
    .stApp {
        background-color: #2E003E;
        color: white;
    }
    """,
    unsafe_allow_html=True
)
with st.container():
    st.image(
        "https://raw.githubusercontent.com/agna2103/simple-expert-system/9aff16990de6ec130049b18a2e502c469492b66c/download.webp",
        width=120,
    )
st.title("Persiapan Emosional Pra-Nikah")
st.subheader("AI dalam Psikologi Kelompok 1")
st.write("Selamat datang di aplikasi ini! 💜")
