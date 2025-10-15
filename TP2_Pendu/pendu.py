import time

from donnees import CHANCES_POSSIBLES
from fonctions import (
    choisir_mot,
    recup_lettre,
    recup_mot_joueur,
    recup_pseudo,
    recup_scores,
    enreg_scores,
)


def main():
    # 1. Nom du joueur
    pseudo = recup_pseudo()

    # 2. Récuperer son score
    scores = recup_scores()
    if pseudo not in scores.keys():  # Nouveau joueur
        scores[pseudo] = 0  # Initialisation du score

    print(f"Bonjour {pseudo}. Vous avez un score de {scores[pseudo]} points.")
    time.sleep(1)  # Simule temps de parole

    # 3. Loop du jeu
    continuer_jeu = True
    while continuer_jeu:

        print("Une nouvelle partie va débuter...")
        time.sleep(1)  # Simule temps de parole

        # 3.1. Choisir un mot
        mot_cible = choisir_mot()
        lettres_trouvees = []
        mot_joueur = recup_mot_joueur(mot_cible, lettres_trouvees)
        chances_restantes = CHANCES_POSSIBLES

        # 3.2. Loop de la partie
        while mot_joueur != mot_cible and chances_restantes > 0:
            print(f"{mot_joueur} (reste {chances_restantes} coup(s))")
            # 3.2.1. Proposer lettre
            lettre = recup_lettre(lettres_trouvees)
            lettres_trouvees.append(lettre)
            lettres_trouvees.sort()
            # 3.2.2. Vérifier lettre
            if lettre in mot_cible:
                print("Bien joué ! Une nouvelle lettre a été ajoutée au mot.")
                mot_joueur = recup_mot_joueur(mot_cible, lettres_trouvees)
            else:
                print("Dommage...")
                chances_restantes -= 1
            time.sleep(1)

        # 3.2.3. Victoire ou défaite ?
        if mot_joueur == mot_cible:
            print(
                f"Félicitation ! Vous avez trouvé le mot {mot_cible}"
                "et il vous restait {chances_restantes} chances."
            )
            # 3.2.3.1. Mettre à jour le score si victoire
            scores[pseudo] += chances_restantes
            time.sleep(1)
            print(f"Votre score total augmente à {scores[pseudo]}.")

        else:
            print(f"Oh non, vous avez perdu... Le mot à deviner était `{mot_cible}`")

        # 3.4. Continuer à jouer ?
        while True:
            reponse = input(">> Souhaitez-vous rejouer ? (o/n) ").lower()
            if reponse == "o":
                continuer_jeu = True
                break
            if reponse == "n":
                continuer_jeu = False
                print("Merci d'avoir joué, au revoir.")
                break
            print("Entrée non reconnue. Veuillez répondre par 'o' ou 'n'.")

    # 4. Màj fichier score
    print(f"Sauvegarde de votre score ({scores[pseudo]}) en cours...")
    enreg_scores(scores)
    time.sleep(1.5)


if __name__ == "__main__":
    main()
