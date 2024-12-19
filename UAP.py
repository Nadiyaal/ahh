import streamlit as st
import tensorflow as tf
import numpy as np
from pathlib import Path
import joblib
import base64

# Konfigurasi halaman utama
st.set_page_config(page_title="Klasifikasi Teks Sentimen", page_icon="🖍", layout="centered")

# Menambahkan gambar latar belakang menggunakan CSS
image_path = Path(__file__).parent / "UAP.jpg"  # Ganti dengan path gambar Anda
if image_path.is_file():
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            color: black;
            font-weight: bold;
        }}
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p {{
            color: black;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("🚨 Gambar latar belakang tidak ditemukan. Pastikan file `UAP.jpg` tersedia di folder aplikasi.")

# Judul aplikasi
st.title("🖍 Klasifikasi Teks Sentimen *Selamat Datang di Aplikasi Klasifikasi Sentimen Berbasis AI!*")

# Menampilkan gambar pendukung
image_path = Path(__file__).parent / "saham.jpg"
if image_path.is_file():
    st.image(str(image_path), width=400)
else:
    st.warning("🚨 Gambar tidak ditemukan. Pastikan file `saham.jpg` tersedia di folder aplikasi.")

# Input teks dari pengguna
text = st.text_area(
    "✍️ **Silakan masukkan teks yang ingin Anda analisis:**",
    placeholder="Contoh: Produk ini luar biasa! Kualitasnya sangat memuaskan. 😊",
    height=150
)

# Fungsi prediksi sentimen
def prediction(input_text):
    try:
        tokenizer_path = Path(__file__).parent / "model/tokenizer.joblib"
        model_path = Path(__file__).parent / "model/model_lstm.h5"

        if not tokenizer_path.is_file() or not model_path.is_file():
            st.error("❌ Tokenizer atau model tidak ditemukan.")
            return None

        tokenizer = joblib.load(tokenizer_path)
        model = tf.keras.models.load_model(model_path)

        if not input_text.strip():
            st.warning("⚠️ Teks tidak boleh kosong!")
            return None

        sequences = tokenizer.texts_to_sequences([input_text])
        pad_seq = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=100, padding='post')

        # Prediksi model
        raw_pred = model.predict(pad_seq, verbose=0)
        result = np.argmax(raw_pred, axis=1)[0]  # Output: 0 (Negatif), 1 (Netral), 2 (Positif)
        return result
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")
        return None

# Tombol untuk menganalisis sentimen
if st.button("🔍 **Analisis Sentimen**"):
    st.subheader("📊 **Hasil Analisis Sentimen**")
    classes = ["❌ Negatif", "🔘 Netral", "✅ Positif"]

    # Efek loading dengan animasi
    with st.spinner("⏳ **AI sedang menganalisis teks Anda...**"):
        progress = st.progress(0)
        for percent_complete in range(1, 101):
            progress.progress(percent_complete / 100)
        result = prediction(text)

    if result is None:
        st.error("⚠️ Gagal memproses prediksi.")
    else:
        if result == 0:
            st.markdown(f"<h3 style='color: red; font-weight: bold;'>Hasil: {classes[result]}</h3>", unsafe_allow_html=True)
            st.snow()  # Efek salju untuk negatif
        elif result == 1:
            st.markdown(f"<h3 style='color: orange; font-weight: bold;'>Hasil: {classes[result]}</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color: green; font-weight: bold;'>Hasil: {classes[result]}</h3>", unsafe_allow_html=True)
            st.balloons()  # Efek balon untuk positif

        # Rincian tambahan dengan kotak latar belakang hitam
        with st.expander("🔎 **Lihat Detail Analisis**"):
            st.markdown(
                f"""
                <div style="background-color: black; padding: 20px; border-radius: 10px;">
                    <p style="color: white; font-weight: bold;">**Teks Anda:** {text}</p>
                    <p style="color: white; font-weight: bold;">**Klasifikasi Sentimen:** {classes[result]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Pesan kembali ke halaman utama
st.markdown(
    """
    🏠 Klik tombol di bawah untuk kembali ke halaman utama!
    """,
    unsafe_allow_html=True
)
if st.button("🔙 **Kembali ke Halaman Utama**"):
    st.info("**Aplikasi siap untuk analisis teks berikutnya! 🚀**")

# Mengubah warna tombol "Analisis Sentimen" menjadi merah
st.markdown(
    """
    <style>
    .stButton>button {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)
