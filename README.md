Customer Support Chatbot Using ML (LSTM & Django)
This repository contains a Customer Support Chatbot powered by Machine Learning, specifically utilizing Long Short-Term Memory (LSTM) models for natural language processing. The backend is built using Django to handle API requests and serve the chatbot to users.

Features
LSTM-based chatbot: Uses an LSTM neural network for intent classification and generating responses.
Django API: Provides RESTful API endpoints to communicate with the chatbot.
Preprocessing: Data preprocessing, tokenization, and text vectorization are handled to make the input data suitable for training.
Customizable: Easily extendable to add more intents and responses based on your requirements.
Table of Contents
Installation
Usage
Project Structure
Model Training
API Endpoints
Contributing
License
Installation
Prerequisites
Python 3.x
Django
TensorFlow/Keras
Numpy
Scikit-learn
Steps to Install
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Setup Django:

bash
Copy code
python manage.py migrate
python manage.py runserver
Usage
Training the Model: The LSTM model needs to be trained using the training_data directory which contains labeled data (questions and corresponding intents). The training script will preprocess the data, train the LSTM model, and save the trained model for inference.

bash
Copy code
python train_model.py
Running the Django Server: After training the model, you can start the Django server to serve the chatbot API.

bash
Copy code
python manage.py runserver
Interacting with the Chatbot: You can interact with the chatbot through a web interface or use the API endpoints to send messages and receive responses.

Project Structure
graphql
Copy code
customer-support-chatbot/
├── chatbot/                  # Main app
│   ├── migrations/
│   ├── models.py             # Django models (if needed)
│   ├── views.py              # Views to handle API requests
│   ├── urls.py               # URL routing for the app
│   ├── serializers.py        # Serializer for API responses
│   └── ...
├── data/                     # Directory containing training data
│   ├── intents.json          # JSON file with predefined intents and responses
│   └── ...
├── model/                    # Directory to store trained models
│   ├── model.h5              # Saved LSTM model
│   └── tokenizer.pickle      # Tokenizer for text preprocessing
├── train_model.py            # Script to train the LSTM model
├── requirements.txt          # List of Python dependencies
├── manage.py                 # Django management script
└── README.md                 # Project documentation
Model Training
Training Data: The training data is stored in data/intents.json and contains sample user queries and corresponding intents. The model learns from this data and maps user inputs to intents.

Training Process: The training process involves:

Data Preprocessing: Tokenizing the text, padding sequences, etc.
Model Creation: An LSTM model built using Keras.
Training: Using the preprocessed data to train the model.
To train the model, run the following command:

bash
Copy code
python train_model.py
Model Evaluation: Once the model is trained, it is saved to the model/ directory as model.h5 for future inference.

API Endpoints
POST /chatbot/message:
Description: Send a message to the chatbot and receive a response.
Request body:
json
Copy code
{
  "message": "Hello, how can I reset my password?"
}
Response:
json
Copy code
{
  "response": "You can reset your password by clicking on 'Forgot Password' at the login page."
}
