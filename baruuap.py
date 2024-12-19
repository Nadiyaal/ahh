# Contoh pengujian langsung
from keras.models import load_model # type: ignore
import joblib
import numpy as np
from keras.preprocessing.sequence import pad_sequences # type: ignore

# Load tokenizer dan model
tokenizer = joblib.load("model/tokenizer.joblib")
model = load_model("model/model_lstm.h5")

# Input contoh teks
sample_text = "Produk ini sangat JELEK dan tidak memuaskan."
sequences = tokenizer.texts_to_sequences([sample_text])
pad_seq = pad_sequences(sequences, maxlen=100, padding='post')

# Prediksi
pred = model.predict(pad_seq)
print("Prediksi mentah:", pred)
print("Kelas:", np.argmax(pred, axis=1))
