# FORT BOYARD SIMULATOR : Sélène AKDOGAN et Océanne TSANE :
#Dans Fort Boyard, l'épreuve du hasard supervise les défis et guide les joueurs à travers diverses épreuves, tout en étant aussi leur adversaire lors de certaines épreuves. Nous implémenterons des jeux où le joueur s'affronte directement avec le maître du jeu.

# Exercice 3.2.1 : Bonneteau (faible)
# Dans cette épreuve, Le joueur doit deviner sous quel bonneteau se cache la clé parmi trois, avec deux essais, la clé étant placée aléatoirement à chaque essai.

# Donc on implémente une fonction qui gère un jeu où le joueur doit deviner sous quel bonneteau (A, B ou C) se cache la clé en deux tentatives, et déclare la victoire ou la défaite en fonction du résultat. Retourne True si le joueur trouve la clé, sinon False après deux essais.
import random
def bonneteau():
# On définit les bonneteaux possibles (A, B, C)
    L= ['A', 'B', 'C']
#On initialise le compteur de tentatives
    tentative=0
    value=random.choice(L)

#On affiche les règles du jeu
    print("Bienvenue à tous au jeu du bonneteau ! Voici les règles du jeu : Vous devez deviner sous quel bonneteau (A,B ou C) se cache la clé. Vous disposez de deux essais pour le trouver.")
    print("Effectuez un choix entre les bonneteaux suivants : A, B ou C")

#Tant que le joueur n'a pas fait deux tentatives, on demande de choisir un bonneteau
    while tentative<2:
        choix_joueur=input("Tentative numéro : {}, choisissez une lettre correspondant au bonnetau parmis A, B ou C : ".format(tentative))

#Si le choix est invalide, on lui demande de réessayer
        if choix_joueur not in L:
            print("Choix invalide. Veuillez choisir parmi A, B ou C :")

#Si le joueur trouve la clé, on affiche un message de victoire
        if choix_joueur == value:
            print("Félicitations ! Vous avez trouvé le bonneteau {} où se cache la clé en {} essais".format(value,tentative))
            return True
        else:
#Sinon, on lui indique de réessayer
            print("Dommage, la clé ne se trouvait pas sous ce bonneteau. Rééssayez, rien n'est perdu !")
        tentative += 1
    print("Désolé, vous avez perdu. La clé se trouvait sous le bonneteau {}".format(value))
    return False



# Exercice 3.2.2 : Lancer de dés (moyenne)
# Dans cette épreuve, on implémente une fonction jeu_lance_des() qui simule un jeu où le joueur et le maître du jeu lancent chacun deux dés, et le premier à obtenir un 6 dans un maximum de trois essais remporte la partie. La fonction retourne True si le joueur gagne, et False si le maître gagne ou si aucun d'eux ne remporte après trois essais..

import random
def jeu_lance_des():
    max=3    #On définit un nombre maximum d'essais

#Boucle principale du jeu qui se répète jusqu'à 3 essais
    for essai in range(max):
        essais_restants= max - essai
        print("Il reste {} essais".format(essais_restants))

#Lancer des dés pour le joueur
        input("Appuyez sur 'Entrée' pour lancer les dés du joueur")

        des1_joueur = random.randint(1, 6)
        des2_joueur = random.randint(1, 6)
        tuple_joueur = (des1_joueur, des2_joueur)
        print("Le joueur a obtenu : {} et {}".format(des1_joueur, des2_joueur))
#Vérification si le joueur a obtenu un 6
        if 6 in tuple_joueur:
            print("Félicitations ! Le joueur a obtenu un 6 et remporte la partie et la clé.")
            return True
#Lancer des dés pour le maître du jeu
        input("Appuyez sur 'Entrée' pour lancer les dés du maître du jeu")
        des1_maitre = random.randint(1, 6)
        des2_maitre = random.randint(1, 6)
        tuple_maitre = (des1_maitre, des2_maitre)
        print("Le maître du jeu a obtenu : {} et {}".format(des1_maitre, des2_maitre))
#Vérification si le maître du jeu a obtenu un 6
        if 6 in tuple_maitre:
            print("Le maître du jeu a obtenu un 6 et remporte la partie")
            return False
#Si aucun joueur n'a obtenu de 6, on passe à l'essai suivant
        print("Aucun joueur n'a obtenu un 6. Passons au prochain essai.")
#Si les trois essais sont écoulés sans gagnant, on déclare un match nul
    print("Aucun joueur n'a obtenu un 6 après trois essais. C'est un match nul.")
    return False


#Exercice 3.2.3 : Fonction epreuve_hasard() pour la sélection aléatoire d'une épreuve
#Pour finir, la dernière épreuve sélectionne une épreuve parmi plusieurs, l'exécute et retourne le résultat (True ou False) en fonction de la réponse du joueur.

def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)

    return epreuve()









