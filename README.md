# ai_chatbot_project1
# 🤖 AI Powered Chatbot (Machine Learning Based)

This is a **simple AI-powered chatbot** built using **Python**, **Flask**, **NLTK**, and **Scikit-learn (ML)**. It takes user queries and responds based on trained intents from `intents.json`.

---

## 📁 Project Structure

ai_chatbot_project/
├── static/
│ └── style.css
├── templates/
│ ├── index.html
│ └── chat.html
├── data/
│ ├── intents.json
│ ├── chatbot_model.pkl
│ ├── classes.pkl
│ ├── words.pkl
│ └── vectorizer.pkl
├── chatbot_model.py
├── app.py
└── README.md

yaml
Copy
Edit

---

## 🧠 Features

- Chatbot built using **Natural Language Processing**
- **Naive Bayes ML algorithm** used for classification
- Friendly web interface with **Flask**
- Trained on a customizable `intents.json` file
- Clean design with CSS styling

---

## 🔧 Requirements

- Python 3.7 or above
- Flask
- scikit-learn
- nltk

### Install them using:

```bash
pip install flask nltk scikit-learn
📥 Training the Model
Run the following to train and generate model files:

bash
Copy
Edit
python chatbot_model.py
This will generate:

chatbot_model.pkl

words.pkl

classes.pkl

vectorizer.pkl

🚀 Running the Chatbot
Start the Flask server:

bash
Copy
Edit
python app.py
Then open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000/
🗃️ Dataset: intents.json
This file contains various intents like:

greeting

goodbye

thanks

name_query

weather

creator, etc.

✍️ Author
Your Name – https://github.com/Sandhyagithub29

📄 License
This project is open-source and free to use for educational purposes
