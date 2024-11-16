import json
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.preprocessing import LabelEncoder
import pickle

# Load intents data
with open('intents.json') as file:
    data = json.load(file)

# Prepare sentences and labels
sentences = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern)
        labels.append(intent['tag'])

# Encode labels
label_encoder = LabelEncoder()
output_data = label_encoder.fit_transform(labels)

# Tokenize words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
vocab_size = len(tokenizer.word_index) + 1

# Convert sentences to sequences and pad them
sequences = tokenizer.texts_to_sequences(sentences)
input_data = pad_sequences(sequences, padding='post')

# Define model
model = Sequential([
    Embedding(vocab_size, 128, input_length=input_data.shape[1]),
    LSTM(64),
    Dense(32, activation='relu'),
    Dense(len(set(labels)), activation='softmax')
])

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
history = model.fit(input_data, output_data, epochs=200, batch_size=5, verbose=1)

# Save model and preprocessing objects
model.save("chatbot_model.keras")
with open("tokenizer.pkl", "wb") as file:
    pickle.dump(tokenizer, file)
with open("label_encoder.pkl", "wb") as file:
    pickle.dump(label_encoder, file)

