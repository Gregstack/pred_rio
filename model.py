import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Charger les données
data = pd.read_csv('/Users/greg/Workspace/RIO Poc item/rioclean2.csv', sep=';', encoding='ISO-8859-1')


# Préparer les données
X = data[['Nom fournisseur','Designation']]
y = data['Concatenation']
X_combined = X['Nom fournisseur'] + ' ' + X['Designation']

# Vectorizer TF-IDF
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X_combined)

# Diviser en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Entraîner le modèle de régression logistique
model = LogisticRegression()
model.fit(X_train, y_train)

# Faire des prédictions
y_pred = model.predict(X_test)

# Évaluer la performance du modèle
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Afficher les résultats
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)

# Sauvegarder le modèle et le vectorizer dans des fichiers pickle
with open('modele_ml.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

"""
Une accuracy de 0,62 indique que le modèle a des difficultés à classer correctement certaines catégories, particulièrement celles qui sont sous-représentées dans le dataset. Voici quelques approches pour améliorer la performance de votre modèle :

1. Équilibrage des classes :
Éliminer les classes sous-représentées : Si certaines classes n'ont qu'une poignée d'exemples (par exemple, moins de 5 ou 10), cela peut nuire à la performance globale du modèle. Envisagez de les éliminer si elles ne sont pas critiques.
Rééchantillonnage :
Oversampling : Augmentez le nombre d'exemples pour les classes sous-représentées en dupliquant des exemples existants ou en utilisant des techniques comme SMOTE (Synthetic Minority Over-sampling Technique).
Undersampling : Réduisez le nombre d'exemples pour les classes sur-représentées. Cela peut aider à équilibrer le dataset, mais vous risquez de perdre des informations précieuses.
2. Modèles spécifiques aux classes :
Utilisez des modèles qui gèrent mieux le déséquilibre des classes, comme les arbres de décision, les forêts aléatoires, ou des modèles de boosting.
3. Pondération des classes :
Modifiez la fonction de perte pour qu'elle prenne en compte le déséquilibre des classes. Par exemple, en ajustant les poids des classes lors de l'entraînement.
4. Analyse des classes :
Examinez les classes qui ont des précisions (precision) et des rappels (recall) faibles. Cela peut vous donner des indices sur lesquelles concentrer vos efforts d'amélioration.
5. Collecte de données supplémentaires :
Si possible, collectez davantage de données pour les classes sous-représentées afin d'améliorer leur représentativité.
Recommandation sur les seuils de sous-représentation :
Taille minimale des classes : Éliminez les classes ayant moins de 5 à 10 exemples.
Considérez l'impact métier : Évaluez si les classes que vous envisagez de retirer sont importantes pour votre modèle ou votre entreprise.
Conclusion
Testez plusieurs approches et évaluez la performance de votre modèle à chaque fois. L'utilisation d'une métrique comme le F1-score peut également être plus informative dans des cas de déséquilibre des classes.

"""