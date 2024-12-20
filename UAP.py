import subprocess
import streamlit as st
import tensorflow as tf
import numpy as np
from pathlib import Path
import joblib
import base64

# Konfigurasi halaman utama
st.set_page_config(page_title="Klasifikasi Teks Sentimen", page_icon="🖍", layout="centered")

# Mengonversi gambar latar belakang menjadi Base64
image_path = Path(__file__).parent / "UAP.jpg"  # Ganti dengan path gambar Anda
if image_path.is_file():
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    background_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}
    .stTitle {{
        color: black !important;  
        font-weight: bold;
        text-align: center;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
else:
    st.error("⚠️ Gambar latar belakang tidak ditemukan!")

st.markdown("<h1 class='stTitle'>🖍 Klasifikasi Teks Sentimen🖍  Selamat Datang di Aplikasi Klasifikasi Sentimen Berbasis AI!</h1>", unsafe_allow_html=True)

text = st.text_area(
    "✍️ **Silakan masukkan teks yang ingin Anda analisis:**",
    placeholder="Contoh: Produk ini luar biasa! Kualitasnya sangat memuaskan. 😊",
    height=150
)

def prediction(input_text):
    if not input_text.strip():
        st.warning("⚠️ Teks tidak boleh kosong!")
        return None
    
    try:
        tokenizer = joblib.load(Path(__file__).parent / "model/tokenizer.joblib")
        model = tf.keras.models.load_model(Path(__file__).parent / "model/model_lstm.h5")
        
        sequences = tokenizer.texts_to_sequences([input_text])
        pad_seq = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=100, padding='post')

        # Prediksi mentah (probabilitas untuk setiap kelas)
        raw_pred = model.predict(pad_seq, verbose=0)[0]
        
        # Menampilkan raw prediction untuk debugging
        st.write(f"Raw Prediction (Probabilitas): {raw_pred}")
        
        # Menentukan hasil prediksi berdasarkan probabilitas tertinggi
        max_prob = np.max(raw_pred)
        
        if max_prob < 0.3:
            return 2  # Netral jika probabilitas terlalu rendah

        # Menggunakan argmax untuk mendapatkan kelas dengan probabilitas tertinggi
        result = np.argmax(raw_pred)  # Output: 0 (Negatif), 1 (Positif), 2 (Netral)
        return result
    
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")
        return None

if st.button("🔍 Analisis Sentimen"):
    st.subheader("📊 Hasil Analisis Sentimen")
    classes = ["❌ Negatif (0)", "✅ Positif (1)", "🔘 Netral (2)"]

    with st.spinner("⏳ Memproses teks Anda..."):
        progress = st.progress(0)
        for percent_complete in range(1, 101):
            progress.progress(percent_complete / 100)
        result = prediction(text)

    if result is None:
        st.error("⚠️ Gagal memproses prediksi.")
    else:
        if result == 0:
            st.markdown(f"<h3 style='color: red;'>Hasil: {classes[result]}</h3>", unsafe_allow_html=True)
            st.snow()  # Efek salju untuk negatif
        elif result == 1:
            st.markdown(f"<h3 style='color: green;'>Hasil: {classes[result]}</h3>", unsafe_allow_html=True)
            st.balloons()  # Efek balon untuk positif
        else:
            st.markdown(f"<h3 style='color: orange;'>Hasil: {classes[result]}</h3>", unsafe_allow_html=True)

        with st.expander("📖 Detail Hasil Prediksi"):
            st.write(f"Teks yang dimasukkan: **{text}**")
            st.write(f"Klasifikasi Sentimen: **{classes[result]}**")

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

if st.button("🔙 Kembali ke Halaman Utama"):
    subprocess.run(["streamlit", "run", "app.py"])
    st.write("**Aplikasi kembali dijalankan!**")
