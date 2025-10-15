"""
Ce fichier définit toutes les données nécessaires à l'exécution du pendu.
Elles sont stockées sous forme de variables.
"""

from pathlib import Path

CHANCES_POSSIBLES = 8

NOM_FICHIER_SCORE = Path(__file__).resolve().parent / "players_scores"

# Les mots sont composés de 8 lettres au maximum
MOTS_POSSIBLES: list[str] = [
    "abeille",
    "gourde",
    "casque",
    "bureau",
    "ville",
    "stylo",
    "couteau",
    "lion",
    "torchon",
    "lampe",
    "poisson",
    "ciel",
    "ampoule",
]
