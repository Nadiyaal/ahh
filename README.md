# ✨ Analisis Sentimen Berita Ekonomi di Twitter CNBC Indonesia untuk Memperkirakan Pergerakan Harga Saham di Indonesia ✨

## 📑 Table of Contents
1. [📋 Deskripsi Proyek](#deskripsi-proyek)
2. [⚙️ Langkah Instalasi](#langkah-instalasi)
3. [🗂️ Overview Dataset](#overview-dataset)
4. [🧠 Deskripsi Model](#deskripsi-model)
   - [📈 LSTM](#lstm)
   - [📊 BERT](#bert)
5. [📊 Hasil dan Analisis](#hasil-dan-analisis)
6. [📊 Kesimpulan perbandingan model LSTM dan BERT](#Kesimpulan-perbandingan-model-LSTM-dan-BERT)
7. [🔗 Link Live Demo](#link-live-demo)
8. [👨‍💻 Author](#author)

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
   git push -u origin main

   commit
   git status
   git add (sesuai file yang ditambahkan)
   git commit -m "coba"
   git push origin main
  
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
| Embedding                | (None, 100, 256)      | 1,280,000            |
| LSTM                     | (None, 256)           | 525,312              |
| Dense                    | (None, 3)             | 771                  |



#### 📊 Hasil Evaluasi Model LSTM
   1. **Training Accuracy**: Sangat tinggi, lebih dari 100%.
   2. **Validation Accuracy**: Stabil di sekitar 85%, menunjukkan kemampuan model untuk menggeneralisasi dengan baik.
   3. **Testing Accuracy**: Sedikit lebih rendah (82%), yang dapat menunjukkan tantangan dalam generalisasi pada data yang lebih bervariasi atau berbeda dari data pelatihan.

#### 📝 Classification Report LSTM

| Label | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.89      | 0.90   | 0.89     | 4925    |
| 1     | 0.66      | 0.59   | 0.62     | 871     |
| 2     | 0.63      | 0.64   | 0.64     | 1002    |

Accuracy: 82%

#### 📉 Grafik Akurasi LSTM

![image](https://github.com/user-attachments/assets/3532e560-be20-4637-b592-70193d31c729)

Training accuracy meningkat secara signifikan dan mencapai hampir 100% setelah beberapa epoch. Testing accuracy stabil di sekitar 83%, menunjukkan adanya sedikit overfitting. 

#### 📉 Grafik Loss LSTM

![image](https://github.com/user-attachments/assets/d513718a-6fd7-4602-93f9-fd5440756dc7)

Training loss terus menurun secara konsisten. Testing loss meningkat setelah beberapa epoch, menandakan adanya overfitting. 

#### 🧩 Confusion Matrix 📊
Hasil dari Confusion Matrix

![image](https://github.com/user-attachments/assets/559b97a4-ca57-4b20-9808-1ab7881c06c5)


#### 🔗 Link Google Colab
Untuk akses notebook Google Colab, klik tautan berikut:  

https://colab.research.google.com/drive/1MsFQt9TNeomKSAOpfp-p-lakFaDSQ47k#scrollTo=AdYreKCqJKw_

### 📊 BERT
Model BERT (Bidirectional Encoder Representations from Transformers) digunakan untuk memanfaatkan representasi teks berbasis transformer yang lebih kaya. Model ini sangat efektif dalam memahami konteks dua arah dalam teks.

#### 🧠 Struktur LSTM 
Arsitektur BERT terdiri dari tiga bagian utama: input layer yang menggabungkan token, segment, dan position embeddings; encoder berbasis Transformer dengan self-attention untuk pemrosesan bidirectional; dan output layer yang menghasilkan representasi vektor untuk tugas lanjutan seperti klasifikasi atau NER.

Berikut adalah ilustrasi struktur BERT: 

![image](https://github.com/user-attachments/assets/583004e0-9546-47c4-bb65-26435c08936d)


#### 🔧Prepocessing 

Pada tahap preprocessing  mencakup data cleaning untuk menghilangkan noise atau data yang tidak relevan, tokenisasi untuk memecah teks menjadi kata atau token, dan stopword removal untuk menghapus kata-kata yang tidak penting seperti "dan", "atau", dan "adalah". dilanjut dengan melakukan splitting dataset menjadi 2 (Training, dan Testing) sesuai dengan penjelasan pada Dataset.

#### 📊 Hasil Evaluasi Model BERT
1. **Training Accuracy**: Meningkat secara signifikan dari 77.52% ke 89.25%.
2. **Validation Accuracy**: Stabil di sekitar 80%-85%, mencerminkan kemampuan model untuk menggeneralisasi data yang tidak terlihat.
3. **Testing Accuracy**: Sekitar 84%, menandakan bahwa model cukup baik dalam melakukan prediksi pada data baru setelah pelatihan.

#### 📝 Classification Report BERT
| Label | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.65      | 0.77   | 0.70     | 890     |
| 1     | 0.70      | 0.70   | 0.70     | 1013    |
| 2     | 0.93      | 0.93   | 0.90     | 4894    |

#### 📉 Grafik BERT

1. **Accuracy:**
   
![image](https://github.com/user-attachments/assets/ed2f75f5-c69b-4d63-a9c3-663729a840a1)
Training accuracy meningkat pesat hingga hampir 95%, dengan testing accuracy stabil di sekitar 92%, menunjukkan model BERT dapat menggeneralisasi dengan baik.

3. **Loss:**
   
![image](https://github.com/user-attachments/assets/4ccde93a-4bb8-4aa8-9ca4-b53cf55c141e)
Training loss terus menurun, sementara testing loss sedikit meningkat, menandakan adanya sedikit overfitting, namun tidak signifikan.


---

#### 🧩 Confusion Matrix 📊
Hasil dari Confusion Matrix

![image](https://github.com/user-attachments/assets/babcb283-66d9-4840-8b17-c7813e391b38)

#### 🔗 Link Google Colab
Untuk akses notebook Google Colab, klik tautan berikut: 

https://colab.research.google.com/drive/1UzBbQt5mKvm93xSGgXrqX2c2iqXLyTDd#scrollTo=EEtvjmJhS43S

## 📊 Hasil dan Analisis

### 📈 Perbandingan Performa Model
| Model | Training Accuracy | Validation Accuracy | Testing Accuracy |
|-------|-------------------|---------------------|------------------|
| LSTM  | 90%               | 85%                 | 82%              |
| BERT  |77.52% ke 89.25%   | 80%-85%             | 84%              |

---

### 📊 Kesimpulan perbandingan model LSTM dan BERT

1. **Akurasi** :
   - *LSTM* :
     * Akurasi training mencapai 90% dan akurasi test mencapai 82%.
     * Performa bagus dalam menangkap konteks temporal, namun terdapat bukti overfitting karena terdapat kesenjangan antara akurasi training dan test.
   - *BERT*:
     * Akurasi training meningkat menjadi 89,25% dan akurasi test mencapai 84%.
     * Memahami konteks teks dua arah lebih baik daripada LSTM, sehingga menghasilkan generalisasi yang lebih kuat.

2. **Loss**:
   – *LSTM*:
     * Loss training terus menurun, tetapi test pengujian meningkat setelah beberapa epoch. Hal ini menunjukkan bahwa model cenderung overfit. 
  - *BERT*:
    * Loss training terus menurun, dan peningkatan kerugian test relatif kecil, menunjukkan sedikit overfitting namun masih dapat dikelola. 
 
 3. **Kemampuan generalisasi**:
    - *LSTM*: Dapat memahami urutan teks dengan baik, namun cenderung overfit.
    - *BERT*: Model dengan  arsitektur transformator dua arah ini lebih baik dalam memahami hubungan yang kompleks dan menunjukkan kemampuan generalisasi yang lebih baik.

4. **Fleksibilitas penyesuaian**:
   - *LSTM*: Cocok untuk data dengan urutan kronologis yang jelas, namun terbatas dalam memahami hubungan nonlinier yang kompleks.
   - *BERT*: Lebih baik dalam menangani konteks kompleks dan hubungan non-linier, memungkinkan Anda melakukan tugas analisis sentimen terperinci dengan lebih efektif.

### **Kesimpulan akhir**:
Akurasi dan generalisasi yang lebih tinggi untuk analisis sentimen, **BERT** adalah pilihan yang lebih baik daripada **LSTM**. Namun, ketika sumber daya komputasi terbatas, **LSTM** tetap menjadi pilihan yang efisien dan cukup andal.

---

## 🔗 Link Live Demo
Aplikasi web telah di-deploy dan dapat diakses melalui tautan berikut:  
[Live Demo Aplikasi](https://uaplatihan.streamlit.app/)


---

## 👨‍💻 Author  
👨‍💻 [Nadiya Dewi Al Khlifi](https://github.com/Nadiyaal)
