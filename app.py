from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import random
import json

nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()

# Load model and other data
model = pickle.load(open("data/chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("data/words.pkl", "rb"))
classes = pickle.load(open("data/classes.pkl", "rb"))

with open("data/intents.json") as file:
    intents = json.load(file)

# Clean and prepare input
def clean_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens]
    return ' '.join(tokens)

# Generate chatbot response
def get_bot_response(message):
    text = clean_text(message)
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == prediction:
            return random.choice(intent["responses"])
    return "I'm not sure how to respond to that."

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
