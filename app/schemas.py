from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class ModePaiement(str, Enum):
    especes = "especes"
    tmoney = "tmoney"
    flooz = "flooz"
    autre = "autre"


class TransactionCreation(BaseModel):
    """Ce que le commerçant envoie pour enregistrer une vente."""

    montant: int = Field(gt=0, description="Montant en francs CFA", examples=[15000])
    nom_client: str = Field(min_length=1, max_length=100, examples=["Kossi Mensah"])
    produit: str = Field(min_length=1, max_length=200, examples=["Sac de riz 25 kg"])
    mode_paiement: ModePaiement = Field(examples=["tmoney"])
    # Facultative : utile pour une vente saisie hors-ligne et envoyée plus tard
    date: datetime | None = Field(default=None, description="Laisser vide pour « maintenant »")


class TransactionLue(BaseModel):
    """Ce que l'API renvoie pour une transaction."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    montant: int
    nom_client: str
    produit: str
    mode_paiement: str
    date: datetime
