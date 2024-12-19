# ✨ Analisis Sentimen Berita Ekonomi di Twitter CNBC Indonesia untuk Memperkirakan Pergerakan Harga Saham di Indonesia ✨

## 📑 Table of Contents
1. [📋 Deskripsi Proyek](#deskripsi-proyek)
2. [⚙️ Langkah Instalasi](#langkah-instalasi)
3. [🗂️ Overview Dataset](#Overview-Dataset)
4. [🧠 Deskripsi Model](#deskripsi-model)
   - [📈 LSTM](#lstm)
   - [📊 BERT](#bert)
5. [📊 Hasil dan Analisis](#hasil-dan-analisis)
6. [🔗 Link Live Demo](#link-live-demo)
7. [👨‍💻 Author](#author)

---

## 📋 Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan model analisis sentimen pada berita ekonomi di Twitter, khususnya dari akun CNBC Indonesia, untuk memprediksi pergerakan harga saham di Indonesia. 

Analisis ini memanfaatkan data berita yang diunggah pada akun Twitter CNBC Indonesia. Dengan metode ini, sistem dapat mengelompokkan berita berdasarkan sentimen positif, negatif, atau netral, yang kemudian digunakan untuk memperkirakan dampaknya terhadap dinamika harga saham.

---

## ⚙️ Langkah Instalasi

Ikuti langkah-langkah berikut untuk menginstal dependencies dan menjalankan aplikasi:

1. **Clone Repository:**
   ```bash
   git init
   git add .
   git commit -m "Inisialisasi proyek"
   git remote add origin https://github.com/Nadiyaal/UAP_ML.git
   git branch -M main
   git push -u origin main
   ```

2. **Buat Virtual Environment:**
   ```bash
   python -m venv env
   env\Scripts\activate   # Untuk Windows
   ```

3. **Instal Dependencies:**
   ```bash
   pip install pdm
   pdm init
   pdm add streamlit
   pdm add tensorflow
   pdm add joblib
   pdm add scikit-learn
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Web:**
   ```bash
   pdm run start
   ```

Aplikasi akan tersedia di `http://127.0.0.1:5000`.

---
## 🗂️ Overview Dataset
Dataset diambil dari [Master Data File Full Columns](https://github.com/ervandioirzky/analisis-sentimen-indonesia/blob/main/Master%20Data%20File%20Full%20Columns.xlsx). Dataset ini mencakup:
- **Periode Pengumpulan Data:** 06 Juli 2020 hingga 11 Januari 2021
- **Jumlah Variabel:** 5 kolom
- **Jumlah Observasi:** 33.989 baris
  Data dibagi menjadi dua bagian: 80% untuk Training Set dan 20% untuk Testing Set. dimana pada setiap Set, terdapat 3 Label Class yaitu
  - Label "1" menunjukkan bahwa berita memiliki sentimen positif yang dapat berpengaruh terhadap kenaikan harga saham.
  - Label "0" menunjukkan bahwa berita memiliki sentimen negatif yang dapat berpengaruh terhadap penurunan harga saham.
  - Label "2" menunjukkan bahwa berita memiliki sentimen netral yang tidak berpengaruh apapun terhadap pergerakan harga saham.
    
## 🧠 Deskripsi Model

### 📈 LSTM
Model LSTM (Long Short-Term Memory) digunakan untuk menangkap konteks temporal dalam teks. Model ini dirancang untuk memahami hubungan antar kata dalam urutan teks sehingga dapat meningkatkan akurasi klasifikasi sentimen.

#### 🧠 Struktur LSTM 
Model LSTM memiliki arsitektur khusus yang dirancang untuk menangani masalah vanishing gradient dalam jaringan saraf berulang (RNN). Struktur utamanya terdiri dari tiga gerbang utama:  Forget Gate: Memutuskan informasi mana yang akan dilupakan dari memori. Input Gate: Memutuskan informasi baru mana yang akan ditambahkan ke memori. Output Gate: Memutuskan bagian dari memori yang akan dikeluarkan sebagai output.

Berikut adalah ilustrasi struktur LSTM: 

![image](https://github.com/user-attachments/assets/c0801fac-bf4c-417a-ba27-28d797fabfae)

#### 🔧Prepocessing 

Pada tahap preprocessing  mencakup data cleaning untuk menghilangkan noise atau data yang tidak relevan, tokenisasi untuk memecah teks menjadi kata atau token, dan stopword removal untuk menghapus kata-kata yang tidak penting seperti "dan", "atau", dan "adalah". dilanjut dengan melakukan splitting dataset menjadi 2 (Training, dan Testing) sesuai dengan penjelasan pada Dataset.

Hasil dari model lstm yang telah di bangun

| Layer Type               | Output Shape          | Number of Parameters |
|--------------------------|-----------------------|----------------------|
| Embedding                | (None, 100, 128)      | 640,000              |
| LSTM                     | (None, 128)           | 131,584              |
| Dense                    | (None, 3)             | 387                  |



#### 📊 Hasil Evaluasi Model LSTM
1. **Training Accuracy:** Model berhasil mencapai akurasi di atas 90%.
2. **Validation Accuracy:** Stabil di sekitar 85%.
3. **Testing Accuracy:** Hasil akhir model menunjukkan akurasi sebesar **83%** pada dataset testing.

#### 📝 Classification Report LSTM

| Label | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.88      | 0.90   | 0.89     | 4925    |
| 1     | 0.93      | 0.91   | 0.92     | 871     |
| 2     | 0.87      | 0.89   | 0.88     | 1002    |

Accuracy: 83%

Macro Average: Precision = 0.74, Recall = 0.73, F1-Score = 0.73 Weighted Average: Precision = 0.83, Recall = 0.83, F1-Score = 0.83 

#### 📉 Grafik Akurasi LSTM

![image](https://github.com/user-attachments/assets/5fb1703f-50f0-4196-b81b-d622c2fa9fce)

Training accuracy meningkat secara signifikan dan mencapai hampir 100% setelah beberapa epoch. Testing accuracy stabil di sekitar 83%, menunjukkan adanya sedikit overfitting. 

#### 📉 Grafik Loss LSTM

![image](https://github.com/user-attachments/assets/73ee70e3-1aca-40ae-9c4b-317eb4c016a5)

Training loss terus menurun secara konsisten. Testing loss meningkat setelah beberapa epoch, menandakan adanya overfitting. 

#### 🧩 Confusion Matrix 📊
Hasil dari Confusion Matrix

![image](https://github.com/user-attachments/assets/5b5c959f-fd7d-4ace-ac4b-b7b0b4c2b864)

#### 🔗 Link Google Colab
Untuk akses notebook Google Colab, klik tautan berikut:  
[Google Colab Notebook](https://colab.research.google.com/drive/11zsktHJstrSbi9ofArmoVHHhPUtJavFw?hl=id#scrollTo=axwcMYbUMUcI&uniqifier=1)

### 📊 BERT
Model BERT (Bidirectional Encoder Representations from Transformers) digunakan untuk memanfaatkan representasi teks berbasis transformer yang lebih kaya. Model ini sangat efektif dalam memahami konteks dua arah dalam teks.

#### 🧠 Struktur LSTM 
Arsitektur BERT terdiri dari tiga bagian utama: input layer yang menggabungkan token, segment, dan position embeddings; encoder berbasis Transformer dengan self-attention untuk pemrosesan bidirectional; dan output layer yang menghasilkan representasi vektor untuk tugas lanjutan seperti klasifikasi atau NER.

Berikut adalah ilustrasi struktur BERT: 

![image](https://github.com/user-attachments/assets/583004e0-9546-47c4-bb65-26435c08936d)


#### 🔧Prepocessing 

Pada tahap preprocessing  mencakup data cleaning untuk menghilangkan noise atau data yang tidak relevan, tokenisasi untuk memecah teks menjadi kata atau token, dan stopword removal untuk menghapus kata-kata yang tidak penting seperti "dan", "atau", dan "adalah". dilanjut dengan melakukan splitting dataset menjadi 2 (Training, dan Testing) sesuai dengan penjelasan pada Dataset.

#### 📊 Hasil Evaluasi Model BERT
1. **Training Accuracy:** Model berhasil mencapai akurasi hingga 95%.
2. **Validation Accuracy:** Stabil di sekitar 90%.
3. **Testing Accuracy:** Akurasi model pada dataset testing mencapai **92%**.

#### 📝 Classification Report BERT
| Label | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.88      | 0.90   | 0.89     | 4925    |
| 1     | 0.93      | 0.91   | 0.92     | 871     |
| 2     | 0.87      | 0.89   | 0.88     | 1002    |


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
[Live Demo Aplikasi](https://barutauuu.streamlit.app/)


---

## 👨‍💻 Author
👨‍💻 **Nadiya Dewi Al Khlifi**  
NIM: 202110370311225  
Universitas Muhammadiyah Malang
