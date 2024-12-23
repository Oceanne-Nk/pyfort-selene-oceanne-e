import random
def bonneteau():
    L= ['A', 'B', 'C']
    tentative=0
    value=random.choice(L)

    print("Bienvenue à tous au jeu du bonneteau ! Voici les règles du jeu : Vous devez deviner sous quel bonneteau (A,B ou C) se cache la clé. Vous disposez de deux essais pour le trouver.")
    print("Effectuez un choix entre les bonneteaux suivants : A, B ou C")

    while tentative<2:
        choix_joueur=input("Tentative numéro : {}, choisissez une lettre correspondant au bonnetau parmis A, B ou C : ".format(tentative))

        if choix_joueur not in L:
            print("Choix invalide. Veuillez choisir parmi A, B ou C :")


        if choix_joueur == value:
            print("Félicitations ! Vous avez trouvé le bonneteau {} où se cache la clé en {} essais".format(value,tentative))
            return True
        else:

            print("Dommage, la clé ne se trouvait pas sous ce bonneteau. Rééssayez, rien n'est perdu !")
        tentative += 1
    print("Désolé, vous avez perdu. La clé se trouvait sous le bonneteau {}".format(value))
    return False




import random
def jeu_lance_des():
    max=3


    for essai in range(max):
        essais_restants= max - essai
        print("Il reste {} essais".format(essais_restants))


        input("Appuyez sur 'Entrée' pour lancer les dés du joueur")

        des1_joueur = random.randint(1, 6)
        des2_joueur = random.randint(1, 6)
        tuple_joueur = (des1_joueur, des2_joueur)
        print("Le joueur a obtenu : {} et {}".format(des1_joueur, des2_joueur))
        if 6 in tuple_joueur:
            print("Félicitations ! Le joueur a obtenu un 6 et remporte la partie et la clé.")
            return True

        input("Appuyez sur 'Entrée' pour lancer les dés du maître du jeu")
        des1_maitre = random.randint(1, 6)
        des2_maitre = random.randint(1, 6)
        tuple_maitre = (des1_maitre, des2_maitre)
        print("Le maître du jeu a obtenu : {} et {}".format(des1_maitre, des2_maitre))

        if 6 in tuple_maitre:
            print("Le maître du jeu a obtenu un 6 et remporte la partie")
            return False

        print("Aucun joueur n'a obtenu un 6. Passons au prochain essai.")

    print("Aucun joueur n'a obtenu un 6 après trois essais. C'est un match nul.")
    return False




def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)

    return epreuve()

print(epreuve_hasard())








