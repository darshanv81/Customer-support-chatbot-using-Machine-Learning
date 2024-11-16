import json
import numpy as np
from django.http import JsonResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from django.views.decorators.csrf import csrf_exempt

# Load the trained model and preprocessors
model = load_model("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/chatbot_model.keras")

# Load tokenizer and label encoder
with open("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

with open("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)

# Load intents data for responses
with open("C:/Users/Darshan.v/Desktop/new_project/chatbot_project/chatbot_project/intents.json") as file:
    intents_data = json.load(file)

# Function to process user input and generate a response
def process_user_input(user_input):
    # Tokenize and pad the input text to match the model's expected input
    sequence = tokenizer.texts_to_sequences([user_input])
    padded_sequence = pad_sequences(sequence, maxlen=20, padding='post')

    # Predict the intent using the trained model
    prediction = model.predict(padded_sequence)
    predicted_class_index = np.argmax(prediction, axis=1)[0]

    # Decode the predicted class label to get the corresponding intent
    intent_label = label_encoder.inverse_transform([predicted_class_index])[0]

    # Find the corresponding response from the intents data
    for intent in intents_data['intents']:
        if intent['tag'] == intent_label:
            return np.random.choice(intent['responses'])

    return "Sorry, I couldn't understand that."

# View to handle the chatbot response
@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        if user_input:
            response = process_user_input(user_input)
            return JsonResponse({"response": response})
        else:
            return JsonResponse({"error": "No message provided"}, status=400)


