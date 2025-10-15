"""
Ce fichier définit toutes les fonctions utiles pour le pendu.
Utilise notamment les données du fichiers `donnees.py`
"""

import os
import pickle
from random import choice

from donnees import NOM_FICHIER_SCORE, MOTS_POSSIBLES


def recup_scores() -> dict[str, int]:
    if os.path.exists(NOM_FICHIER_SCORE):
        with open(NOM_FICHIER_SCORE, "rb") as fichier_scores:
            depickler = pickle.Unpickler(fichier_scores)
            scores = depickler.load()
    else:
        scores = {}
    return scores


def enreg_scores(scores: dict[str, int]) -> None:
    with open(NOM_FICHIER_SCORE, "wb") as fichier_scores:
        depickler = pickle.Pickler(fichier_scores)
        depickler.dump(scores)


def recup_pseudo() -> str:
    pseudo = input(">> Entrez votre pseudo: ")
    if len(pseudo) > 10:
        print("Votre pseudo ne doit pas comporter plus de 10 caractères.")
        return recup_pseudo()
    return pseudo


def recup_lettre(lettres_trouvees: list[str]) -> str:
    lettre = input(">> Entrez une lettre: ").lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("Veuillez ne saisir qu'une lettre, issue de l'alphabet")
        return recup_lettre(lettres_trouvees)
    if lettre in lettres_trouvees:
        print(
            "Vous avez déjà essayé cette lettre. Pour rappel, les lettres tentées sont:",
            lettres_trouvees,
        )
        return recup_lettre(lettres_trouvees)
    return lettre


def choisir_mot() -> str:
    return choice(MOTS_POSSIBLES)


def recup_mot_joueur(mot_cible: str, lettres_trouvees: list[str]):
    mot_joueur = ""
    for lettre_mot in mot_cible:
        if lettre_mot in lettres_trouvees:
            mot_joueur += lettre_mot
        else:
            mot_joueur += "*"
    return mot_joueur
