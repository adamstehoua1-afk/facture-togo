from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Au démarrage : crée les tables qui n'existent pas encore (ne touche pas aux données)
    if engine is not None:
        Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="API Facture Togo", lifespan=lifespan)


@app.get("/")
def accueil():
    return {"message": "API Facture Togo opérationnelle"}


@app.get("/health")
def health():
    # Volontairement sans base de données : UptimeRobot l'appelle toutes les 5 minutes
    return {"status": "ok"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        raise HTTPException(status_code=503, detail="Base de données injoignable")
    return {"database": "ok"}


@app.post("/transactions", response_model=schemas.TransactionLue, status_code=201)
def creer_transaction(donnees: schemas.TransactionCreation, db: Session = Depends(get_db)):
    valeurs = donnees.model_dump(exclude_none=True)
    valeurs["mode_paiement"] = donnees.mode_paiement.value
    transaction = models.Transaction(**valeurs)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


@app.get("/transactions", response_model=list[schemas.TransactionLue])
def lister_transactions(
    limite: int = Query(100, ge=1, le=1000, description="Nombre maximum de ventes renvoyées"),
    decalage: int = Query(0, ge=0, description="Nombre de ventes à sauter (pour voir les suivantes)"),
    db: Session = Depends(get_db),
):
    # Les ventes les plus récentes en premier
    return (
        db.query(models.Transaction)
        .order_by(models.Transaction.date.desc(), models.Transaction.id.desc())
        .offset(decalage)
        .limit(limite)
        .all()
    )
