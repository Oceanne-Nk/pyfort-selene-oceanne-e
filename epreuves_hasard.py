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

print(bonneteau())

