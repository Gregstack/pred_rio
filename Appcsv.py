from flask import Flask, render_template, request, send_file
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import io

app = Flask(__name__)

# Charger le modèle et le vecteur TF-IDF
def charger_model():
    with open('modele_ml.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = charger_model()

# Route principale pour afficher le formulaire
@app.route('/')
def index():
    return render_template('indexcsv.html')

# Route pour faire une prédiction sur un fichier CSV
@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    file = request.files['file']
    
    if not file:
        return "Aucun fichier n'a été sélectionné", 400
    
    # Lire le fichier CSV
    df = pd.read_csv(file)
    
    # Vérifier que les colonnes attendues sont présentes
    if 'Nom fournisseur' not in df.columns or 'Designation' not in df.columns:
        return "Le fichier doit contenir les colonnes 'Nom fournisseur' et 'Designation'", 400
    
    # Créer une colonne combinée pour la prédiction
    df['texte'] = df['Nom fournisseur'] + ' ' + df['Designation']
    
    # Transformer le texte avec le vectorizer
    texte_tfidf = vectorizer.transform(df['texte'])
    
    # Faire les prédictions
    df['Prédiction catégorie'] = model.predict(texte_tfidf)
    
    # Garder uniquement les colonnes 'Nom fournisseur', 'Designation' et 'Prédiction catégorie'
    output_df = df[['Nom fournisseur', 'Designation', 'Prédiction catégorie']]
    
    # Préparer le fichier CSV de sortie en mémoire avec BytesIO
    output = io.BytesIO()
    output_df.to_csv(output, index=False, encoding='utf-8')
    output.seek(0)
    
    return send_file(output, mimetype="text/csv", as_attachment=True, download_name="predictions.csv")


if __name__ == '__main__':
    app.run(debug=True)

'''Pour lancer l'application 

// Lance ton application Flask localement (comme tu le fais normalement) :


python app.py

 // Ouvre une nouvelle fenêtre de terminal et exécute ngrok sur le port où Flask est en cours d'exécution (par défaut, Flask utilise le port 5000) :

ngrok http 5000

 // Ngrok te fournira une URL publique comme https://abcd1234.ngrok.io, que tu pourras partager avec ton ami.





'''