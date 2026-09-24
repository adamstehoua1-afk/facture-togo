from sqlalchemy import Column, DateTime, Integer, String, func

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    # En francs CFA : pas de centimes, donc un nombre entier
    montant = Column(Integer, nullable=False)
    nom_client = Column(String(100), nullable=False)
    produit = Column(String(200), nullable=False)
    # Ex. : "especes", "tmoney", "flooz"
    mode_paiement = Column(String(30), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
