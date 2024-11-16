import json
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the model and necessary files
model = load_model("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/chatbot_model.keras")

# Load the tokenizer and label encoder
with open("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

with open("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)

# Load intents data for responses
with open("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/intents.json") as file:
    intents_data = json.load(file)

# Index view to handle both GET (displaying the chatbot) and POST (handling chatbot responses)
def index(request):
    if request.method == "POST":
        user_message = request.POST.get("user_message")
        if user_message:
            response = chatbot_response(user_message)
            return JsonResponse({"response": response})
        else:
            return JsonResponse({"error": "No message provided"}, status=400)
    
    # For GET requests, just render the initial chatbot page
    return render(request, "chatbot/index.html")

# Function to process the user's input and generate a response
def chatbot_response(message):
    # Tokenize and preprocess the user's message
    message_sequence = tokenizer.texts_to_sequences([message])
    message_padded = pad_sequences(message_sequence, maxlen=100, padding='post')

    # Get the model's prediction
    prediction = model.predict(message_padded)
    predicted_label_index = np.argmax(prediction, axis=1)[0]

    # Decode the predicted label to a response
    intent_label = label_encoder.inverse_transform([predicted_label_index])[0]

    # Find the corresponding intent in the intents file and return a random response
    for intent in intents_data['intents']:
        if intent['tag'] == intent_label:
            return np.random.choice(intent['responses'])
    
    return "Sorry, I couldn't understand that."


