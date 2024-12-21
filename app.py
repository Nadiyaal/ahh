import streamlit as st
from pathlib import Path
import base64
import subprocess

# Menambahkan gambar latar belakang menggunakan CSS
image_path = Path(__file__).parent / "image/UAP.jpg"  # Ganti dengan path gambar Anda
if image_path.is_file():
    # Mengonversi gambar ke base64
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    # Menambahkan CSS untuk gambar latar belakang
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}

        .main-header {{
            font-size: 45px;
            background-color: rgba(76, 175, 80, 0.8); /* Transparansi */
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            color: #000000;  /* Warna hitam untuk teks 'Selamat Datang' */
        }}

        .stButton button {{
            background-color: #ff0000; /* Warna merah */
            color: #ffffff; /* Warna teks putih */
            border: none;
            border-radius: 10px; /* Membuat sudut tombol melengkung */
            padding: 10px 20px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
        }}

        .stButton button:hover {{
            background-color: #cc0000; /* Warna merah gelap saat hover */
            transform: scale(1.05); /* Efek zoom kecil saat hover */
        }}

        /* Menambahkan CSS untuk warna hitam dan bold pada teks */
        .black-text {{
            color: #000000;
            font-weight: bold;
        }}

        /* Menambahkan CSS untuk label input */
        .stTextInput label {{
            color: #000000;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning("🚨 Gambar latar belakang tidak ditemukan. Pastikan file `UAP.jpg` tersedia di folder `model`.")

# Header utama
st.markdown('<div class="main-header">✨ Selamat Datang di Ujian Akhir Pratikum Pembelajaran Mesin yang Kreatif! ✨</div>', unsafe_allow_html=True)

# Input nama pengguna
nama = st.text_input("📝 Masukkan Nama Anda:", placeholder="Contoh: Nadiya")

# Menampilkan sambutan personal jika nama dimasukkan
if nama:
    st.markdown(f'<div class="black-text">👋 Selamat Datang, {nama}! 🚀</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="black-text">Selamat datang di platform Ujian Akhir Praktikum. Di sini Anda dapat melakukan klasifikasi teks analisis sentimen, deteksi topik, dan lainnya. 🧠💬</div>',
        unsafe_allow_html=True
    )

    # Card untuk klasifikasi teks
    st.markdown('<div style="text-align:center; margin-top: 20px;">', unsafe_allow_html=True)
    if st.button("Mulai Klasifikasi Teks", key="text_classification", help="Klik untuk mulai klasifikasi teks!"):
        subprocess.run(["streamlit", "run", "UAP.py"])
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="black-text">🚨 Silakan masukkan nama Anda untuk melanjutkan.</div>', unsafe_allow_html=True)
