from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Charger le modèle et le vecteur TF-IDF
def charger_model():
    # Charger ton modèle depuis un fichier pickle
    with open('modele_ml.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

# Charger modèle et vecteur
model, vectorizer = charger_model()

# Route principale pour afficher le formulaire
@app.route('/')
def index():
    return render_template('index.html')

# Route pour faire une prédiction
@app.route('/predict', methods=['POST'])
def predict():
    nom_fournisseur = request.form['nom_fournisseur']
    designation = request.form['designation']
    
    # Créer l'input combiné
    texte = nom_fournisseur + ' ' + designation
    
    # Transformer l'input avec le vectorizer
    texte_tfidf = vectorizer.transform([texte])
    
    # Faire la prédiction
    prediction = model.predict(texte_tfidf)[0]
    
    # Passer les valeurs pour l'affichage dans le template
    return render_template('index.html', 
                           prediction=prediction, 
                           nom_fournisseur=nom_fournisseur, 
                           designation=designation)

if __name__ == '__main__':
    app.run(debug=True)
