# FORT BOYARD SIMULATOR : Sélène AKDOGAN et Océanne TSANE :
#Dans le fichier main.py, nous devons definir la fonction jeu() qui centralisera toutes les actions du jeu en utilisant les fonctions des autres modules que nous avons créés dans ce projet.
import random
import json
from fonctions_utiles import introduction, composer_equipe, menu_epreuves, choisir_joueur
from epreuves_mathematique import epreuve_math
from epreuves_logiques import jeu_tictactoe
from epreuves_hasard import epreuve_hasard
from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_De_Tresor

#La fonction enigme_pere_fouras_fonction() appelle simplement la fonction enigme_pere_fouras() en lui passant en argument le fichier "data/enigmesPF.json".
def enigme_pere_fouras_fonction():
    return enigme_pere_fouras("data/enigmesPF.json")


#La fonction jeu() orchestre le déroulement du jeu, gérant la composition de l'équipe, la sélection des épreuves, et l'attribution des clés, jusqu'à l'épreuve finale où l'équipe tente de déverrouiller la salle du trésor.
def jeu():
    # Étape 1 : Introduction et composition de l'équipe
    introduction()
    equipe = composer_equipe()
    print("\nVotre équipe est composée de :")
    for joueur in equipe:
        print("- {}".format(joueur['nom']))

    # Étape 2 : Boucle des épreuves
    cles_gagnees = 0
    while cles_gagnees < 3:
        print("\nClés gagnées : {}/3".format(cles_gagnees))

        # Menu des épreuves
        choix_epreuve = menu_epreuves()
        epreuve_choisie = 0

        # Sélection de l'épreuve selon le type choisi
        if choix_epreuve == 1:
            print("Vous avez choisi l'épreuve de mathématiques.")
            epreuve_choisie = epreuve_math
        elif choix_epreuve == 2:
            print("Choisissez une autre ")
            epreuve_choisie = jeu_tictactoe
        elif choix_epreuve == 3:
            print("Vous avez choisi l'épreuve du hasard.")
            epreuve_choisie = epreuve_hasard
        elif choix_epreuve == 4:
            print("Vous avez choisi l'énigme du Père Fouras.")
            epreuve_choisie = enigme_pere_fouras_fonction
        else:
            print("Choix invalide, veuillez sélectionner un numéro entre 1 et 4.")



        joueur_selectionne = choisir_joueur(equipe)
        epreuve_reussie = epreuve_choisie()


        if epreuve_reussie:
            print("Bravo, épreuve réussie ! Une clé a été gagnée.")
            joueur_selectionne['cles_gagnees'] += 1
            cles_gagnees += 1
        else:
            print("Dommage, épreuve échouée. Pas de clé cette fois.")

    # Étape 3 : Épreuve finale
    print("\nToutes les clés ont été gagnées ! Place à l'épreuve finale.")
    indices = "data/indicesSalle.json"


    salle_de_tresor_deverrouille = False

    # Vérifier si la fonction salle_De_Tresor renvoie True ou False
    if cles_gagnees == 3:
        salle_de_tresor_resultat = salle_De_Tresor(indices)



jeu()
