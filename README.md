# Facture Togo

Outil de facturation hors-ligne pour les commerçants du Togo.
Ceci est la première brique : une petite API (un « serveur ») qui répond qu'elle fonctionne.

## Contenu du projet

| Fichier | À quoi il sert |
|---|---|
| `app/main.py` | Le cœur de l'API |
| `requirements.txt` | La liste des outils Python nécessaires |
| `render.yaml` | Les réglages pour mettre l'API en ligne sur Render |
| `.env.example` | Un modèle pour l'adresse de la base de données |
| `.gitignore` | Les fichiers à ne jamais envoyer sur GitHub |

## Adresses disponibles

- `/` → affiche `{"message": "API Facture Togo opérationnelle"}`
- `/health` → affiche `{"status": "ok"}` (sert à vérifier que l'API est vivante)
- `/docs` → une page automatique pour tester l'API

## Lancer sur son ordinateur (facultatif)

Il faut avoir installé Python (python.org). Puis, dans un terminal, dans ce dossier :

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Ouvrez ensuite http://127.0.0.1:8000 dans votre navigateur.

## Mettre en ligne sur Render

1. Créez un compte sur https://render.com (connexion avec GitHub).
2. Cliquez sur **New +** → **Blueprint**, puis choisissez ce dépôt.
3. Render lit `render.yaml` et vous demande la valeur de `DATABASE_URL`
   (vous pouvez la laisser vide pour l'instant).
4. Attendez quelques minutes : votre API aura une adresse du type
   `https://facture-togo.onrender.com`.

## Important

Ne mettez jamais votre vrai fichier `.env` sur GitHub : il contient vos mots de passe.
Il est déjà ignoré grâce au fichier `.gitignore`.
