import os

from dotenv import load_dotenv
from fastapi import FastAPI

# Charge les variables du fichier .env (en local uniquement)
load_dotenv()

# Adresse de la base de données (pas encore utilisée)
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI(title="API Facture Togo")


@app.get("/")
def accueil():
    return {"message": "API Facture Togo opérationnelle"}


@app.get("/health")
def health():
    return {"status": "ok"}
