import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Charge les variables du fichier .env (en local uniquement)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Certains fournisseurs donnent une adresse en "postgres://", que SQLAlchemy refuse
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# pool_pre_ping : vérifie la connexion avant usage (Neon coupe les connexions inactives)
engine = (
    create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=300)
    if DATABASE_URL
    else None
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    """Ouvre une session vers la base pour une requête, puis la referme."""
    if engine is None:
        raise RuntimeError("DATABASE_URL n'est pas configurée")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
