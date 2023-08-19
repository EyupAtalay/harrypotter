import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# TensorFlow ve GPU konfigürasyonu
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# Veri oluşturma (örnek olarak rastgele veri kullanıyoruz)
import numpy as np
X_train = np.random.rand(100, 10)  # 100 örnek, her biri 10 özellik
y_train = np.random.randint(2, size=100)  # İkili sınıflandırma için rastgele etiketler

# Model oluşturma
model = Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Modeli derleme
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitme
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Modelin tahmin yapması (örnek veri ile)
sample_data = np.random.rand(5, 10)
predictions = model.predict(sample_data)
print("Tahminler:", predictions)
