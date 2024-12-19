# ✨ Analisis Sentimen Berita Ekonomi di Twitter CNBC Indonesia untuk Memperkirakan Pergerakan Harga Saham di Indonesia ✨

## 📑 Table of Contents
1. [📋 Deskripsi Proyek](#deskripsi-proyek)
2. [⚙️ Langkah Instalasi](#langkah-instalasi)
3. [🧠 Deskripsi Model](#deskripsi-model)
   - [📈 LSTM](#lstm)
   - [📊 BERT](#bert)
4. [📊 Hasil dan Analisis](#hasil-dan-analisis)
5. [🔗 Link Live Demo](#link-live-demo)
6. [👨‍💻 Author](#author)

---

## 📋 Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan model analisis sentimen pada berita ekonomi di Twitter, khususnya dari akun CNBC Indonesia, untuk memprediksi pergerakan harga saham di Indonesia. 

Analisis ini memanfaatkan data berita yang diunggah pada akun Twitter CNBC Indonesia. Dengan metode ini, sistem dapat mengelompokkan berita berdasarkan sentimen positif, negatif, atau netral, yang kemudian digunakan untuk memperkirakan dampaknya terhadap dinamika harga saham.

---

## ⚙️ Langkah Instalasi

Ikuti langkah-langkah berikut untuk menginstal dependencies dan menjalankan aplikasi:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/Nadiyaal/analisis-sentimen-indonesia.git
   cd analisis-sentimen-indonesia
   ```

2. **Buat Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk macOS/Linux
   env\Scripts\activate   # Untuk Windows
   ```

3. **Instal Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Web:**
   ```bash
   flask run
   ```

Aplikasi akan tersedia di `http://127.0.0.1:5000`.

---

## 🧠 Deskripsi Model

### 📈 LSTM
Model LSTM (Long Short-Term Memory) digunakan untuk menangkap konteks temporal dalam teks. Model ini dirancang untuk memahami hubungan antar kata dalam urutan teks sehingga dapat meningkatkan akurasi klasifikasi sentimen.

#### 📊 Hasil Evaluasi Model LSTM
1. **Training Accuracy:** Model berhasil mencapai akurasi di atas 90%.
2. **Validation Accuracy:** Stabil di sekitar 85%.
3. **Testing Accuracy:** Hasil akhir model menunjukkan akurasi sebesar **87%** pada dataset testing.

#### 📝 Classification Report LSTM
| Label | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| 0     | 0.85      | 0.87   | 0.86     |
| 1     | 0.89      | 0.86   | 0.87     |
| -     | 0.80      | 0.83   | 0.81     |

### 📊 BERT
Model BERT (Bidirectional Encoder Representations from Transformers) digunakan untuk memanfaatkan representasi teks berbasis transformer yang lebih kaya. Model ini sangat efektif dalam memahami konteks dua arah dalam teks.

#### 📊 Hasil Evaluasi Model BERT
1. **Training Accuracy:** Model berhasil mencapai akurasi hingga 95%.
2. **Validation Accuracy:** Stabil di sekitar 90%.
3. **Testing Accuracy:** Akurasi model pada dataset testing mencapai **92%**.

#### 📝 Classification Report BERT
| Label | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| 0     | 0.88      | 0.90   | 0.89     |
| 1     | 0.93      | 0.91   | 0.92     |
| -     | 0.87      | 0.89   | 0.88     |

---

## 📊 Hasil dan Analisis

### 📈 Perbandingan Performa Model
| Model | Training Accuracy | Validation Accuracy | Testing Accuracy |
|-------|-------------------|---------------------|------------------|
| LSTM  | 90%               | 85%                 | 87%              |
| BERT  | 95%               | 90%                 | 92%              |

### 📉 Grafik Performa

1. **Accuracy:**
   - Grafik menunjukkan bahwa model BERT memiliki akurasi lebih tinggi dibandingkan LSTM pada validation dan testing.

2. **Loss:**
   - Model BERT memiliki loss yang lebih rendah pada training dan validation dibandingkan LSTM.

---

## 🔗 Link Live Demo
Aplikasi web telah di-deploy dan dapat diakses melalui tautan berikut:  
[Live Demo Aplikasi](#)

---

## 👨‍💻 Author
👨‍💻 **Nadiya Dewi Al Khlifi**  
NIM: 202110370311225  
Universitas Muhammadiyah Malang
