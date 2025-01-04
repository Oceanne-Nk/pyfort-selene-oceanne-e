#Exercice 3.4 : Le module enigme_pere_fouras.py

#L'objectif de cet exercice est d'implémenter deux fonctions simulant une rencontre avec le Père Fouras, où nous devons résoudre une énigme en trois tentatives pour gagner une clé, sinon un message de défaite avec la solution est affiché.

#Nous importons d'abord le module JSON pour travailler avec des données JSON. Puis le module random pour choisir une énigme de manière aléatoire.

import json
import random

#Nous créeons ensuite une fonction pour charger les énigmes à partir d'un fichier JSON.
def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)      #Nous implémentons le contenu du fichier JSON dans une variable 'enigmes'.
    return enigmes

#Nous créeons ensuite une fonction qui simule une rencontre avec le Père Fouras et qui pose une énigme aléatoire au joueur.
def enigme_pere_fouras(fichier):

    enigmes = charger_enigmes(fichier)      #Nous appelons  la fonction 'charger_enigmes'

#Nous sélectionnons aléatoirement une énigme parmi celles chargées dans la liste 'enigmes'.
    enigme_choisie = random.choice(enigmes)


    print("Énigme : {}".format(enigme_choisie['question']))

#Nous initialisons le nombre d'essais restants (3 essais pour résoudre l'énigme).
    essais_restants = 3

    # Nous Demandons au joueur de répondre avec 3 tentatives
    while essais_restants > 0:
        reponse_joueur = input("Votre réponse : ").lower()  # Nous demandons une réponse et convertissons en minuscules

        if reponse_joueur == enigme_choisie['reponse'].lower():  # Nous vérifions la réponse
            print("Bonne réponse ! Vous avez gagné la clé.")
            return True  # Le joueur gagne la clé
        else:
            essais_restants -= 1  # Nous réduisons le nombre d'essais restants
            if essais_restants > 0:
                print("Incorrect ! Il vous reste {} essais.".format(essais_restants))
            else:
                print("Vous avez échoué ! La solution était : {}".format(enigme_choisie['reponse']))
                return False

