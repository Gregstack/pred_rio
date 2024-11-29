
# Application Flask de Prédiction de Catégorie

Cette application Flask permet de prédire des catégories pour des produits en fonction de leur description, à partir d'un fichier CSV. L'application utilise un modèle de machine learning (`modele_ml.pkl`) et un vecteur TF-IDF (`vectorizer.pkl`) pour effectuer les prédictions.

## Prérequis

Avant de commencer, assurez-vous que vous avez installé les dépendances nécessaires dans votre environnement virtuel. Vous pouvez le faire avec `pip` :

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` doit contenir les bibliothèques suivantes :

```
Flask
pandas
scikit-learn
```

## Lancer l'application localement

1. **Lancer l'application Flask :**

   Ouvrez un terminal dans le répertoire de votre projet et exécutez la commande suivante pour démarrer le serveur Flask :

   ```bash
   python app.py
   ```

   Par défaut, Flask s'exécutera sur le port 5000 (http://127.0.0.1:5000).

2. **Lancer ngrok pour exposer l'application :**

   Ouvrez une nouvelle fenêtre de terminal et exécutez la commande suivante pour exposer votre application Flask localement via une URL publique avec ngrok :

   ```bash
   ngrok http 5000
   ```

   Ngrok vous fournira une URL publique comme `http://abcd1234.ngrok.io`, que vous pourrez partager avec d'autres personnes pour qu'elles accèdent à votre application.

## Utilisation de l'application

1. **Accéder à l'application :**

   Une fois l'application lancée, ouvrez votre navigateur et accédez à l'URL publique fournie par ngrok (par exemple : `http://abcd1234.ngrok.io`).

2. **Télécharger un fichier CSV :**

   L'interface de l'application vous permettra de télécharger un fichier CSV. Ce fichier doit contenir les colonnes suivantes :
   - **Nom fournisseur**
   - **Designation**

   Exemple de format CSV :

   ```csv
   Nom fournisseur,Designation
   Fournisseur A,Vis M10
   Fournisseur B,Écrou M10
   ```

3. **Faire une prédiction :**

   Après avoir téléchargé votre fichier CSV, l'application traitera les données et effectuera les prédictions en utilisant le modèle de machine learning. Un fichier CSV de sortie sera généré avec une nouvelle colonne `Prédiction catégorie`.

   Exemple de sortie :

   ```csv
   Nom fournisseur,Designation,Prédiction catégorie
   Fournisseur A,Vis M10,Catégorie 1
   Fournisseur B,Écrou M10,Catégorie 2
   ```

4. **Télécharger le fichier de sortie :**

   Une fois les prédictions effectuées, vous pourrez télécharger le fichier CSV avec les résultats.

## Structure du projet

```
/mon-projet-flask
│
├── app.py                  # Code de l'application Flask
├── modele_ml.pkl           # Modèle de machine learning
├── vectorizer.pkl          # Vecteur TF-IDF
├── templates
│   └── indexcsv.html       # Interface utilisateur pour télécharger le CSV
└── requirements.txt        # Liste des dépendances
```

## Dépannage

- **Erreur de fichier CSV manquant :** Assurez-vous que votre fichier CSV contient les colonnes `Nom fournisseur` et `Designation`.
- **Modèle ou vecteur manquant :** Vérifiez que les fichiers `modele_ml.pkl` et `vectorizer.pkl` sont présents dans le répertoire du projet.

## License

Ce projet est sous [Licence MIT](LICENSE).
```

### Explication :

1. **Prérequis :** Il inclut une section pour installer les dépendances via un fichier `requirements.txt` (si tu choisis d'en créer un).
2. **Lancer l'application :** Les étapes sont décrites pour exécuter Flask et utiliser ngrok pour exposer l'application localement.
3. **Utilisation :** Explique comment télécharger un fichier CSV, obtenir des prédictions, et télécharger le fichier de sortie.
4. **Structure du projet :** Un récapitulatif de la structure des fichiers du projet pour faciliter la navigation.
5. **Dépannage :** Quelques conseils si l'utilisateur rencontre des erreurs courantes.
