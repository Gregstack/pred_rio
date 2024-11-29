Voici un exemple de fichier README pour ton application Flask :

---

# Application de Prédiction de Catégories à partir d'un Fichier CSV

Cette application Flask permet d'effectuer des prédictions de catégories sur un fichier CSV contenant des informations sur des fournisseurs et des désignations de produits. Le modèle de machine learning utilisé pour la prédiction a été préalablement entraîné et est chargé dans l'application.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances suivantes :

- Flask
- pandas
- scikit-learn

Vous pouvez installer ces dépendances avec la commande :

```bash
pip install -r requirements.txt
```

## Fonctionnement de l'application

1. L'utilisateur télécharge un fichier CSV contenant les colonnes `Nom fournisseur` et `Designation`.
2. Le modèle de machine learning, préalablement formé avec un `TfidfVectorizer` et un `LogisticRegression`, effectue des prédictions sur chaque ligne du fichier.
3. Les résultats de prédiction sont ajoutés dans une nouvelle colonne appelée `Prédiction catégorie` et un nouveau fichier CSV avec ces prédictions est généré.
4. Le fichier CSV résultant est disponible en téléchargement pour l'utilisateur.

### Colonnes attendues dans le fichier CSV
Le fichier CSV d'entrée doit contenir les colonnes suivantes :

- `Nom fournisseur` : Le nom du fournisseur.
- `Designation` : La désignation du produit.

Exemple de fichier CSV :

| Nom fournisseur | Designation      |
|-----------------|------------------|
| Fournisseur A   | Vis M8           |
| Fournisseur B   | Écrou M10        |

### Résultat attendu
Après avoir effectué les prédictions, le fichier CSV de sortie contiendra les colonnes suivantes :

- `Nom fournisseur`
- `Designation`
- `Prédiction catégorie` : La catégorie prédite par le modèle pour chaque ligne.

Exemple de fichier CSV de sortie :

| Nom fournisseur | Designation      | Prédiction catégorie |
|-----------------|------------------|----------------------|
| Fournisseur A   | Vis M8           | Catégorie 1          |
| Fournisseur B   | Écrou M10        | Catégorie 2          |

## Lancer l'application

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances avec :

```bash
pip install -r requirements.txt
```

3. Lancez l'application Flask avec la commande :

```bash
python app.py
```

Cela démarrera l'application sur `http://127.0.0.1:5000/`.

## Accès à distance avec Ngrok

Si vous souhaitez accéder à votre application Flask à distance, vous pouvez utiliser **Ngrok** pour exposer votre serveur local à une URL publique.

1. Téléchargez et installez [Ngrok](https://ngrok.com/).
2. Dans une nouvelle fenêtre de terminal, exécutez la commande suivante pour exposer votre application Flask en ligne :

```bash
ngrok http 5000
```

Ngrok générera une URL publique (par exemple, `https://abcd1234.ngrok.io`), que vous pourrez partager avec d'autres utilisateurs.

---

## Structure du projet

```
.
├── app.py               # Fichier principal de l'application Flask
├── modele_ml.pkl        # Modèle de machine learning préalablement entraîné
├── vectorizer.pkl       # Fichier contenant le vectorizer TF-IDF
├── requirements.txt     # Liste des dépendances
└── templates/
    └── indexcsv.html    # Page HTML pour le formulaire de téléchargement de CSV
```

---

## À propos

Cette application utilise un modèle de machine learning préalablement entraîné pour catégoriser les produits en fonction de la désignation et du fournisseur. Le modèle utilise une combinaison de `TfidfVectorizer` et `LogisticRegression` pour effectuer des prédictions textuelles basées sur les colonnes fournies.

---

J'espère que cela répond à ta demande pour un README complet !
