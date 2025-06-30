import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

with open("data/intents.json") as f:
    data = json.load(f)

corpus = []
labels = []
classes = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens]
        corpus.append(' '.join(tokens))
        labels.append(intent['tag'])
    if intent['tag'] not in classes:
        classes.append(intent['tag'])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = labels

model = MultinomialNB()
model.fit(X, y)

# ✅ Save trained components
with open("data/chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("data/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("data/classes.pkl", "wb") as f:
    pickle.dump(classes, f)

# ✅ Final confirmation message
print("✅ Model trained and all files saved successfully.")
