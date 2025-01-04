def afficher_grille(grille):

    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)


def verifier_victoire(grille, symbole):

    for ligne in grille:
        victoire = True
        for case in ligne:
            if case != symbole:
                victoire = False
        if victoire:
            return True


    for col in range(3):
        victoire = True
        for row in range(3):
            if grille[row][col] != symbole:
                victoire = False
        if victoire:
            return True



    victoire_diag1 = True
    for i in range(3):
        if grille[i][i] != symbole:
            victoire_diag1 = False
    if victoire_diag1:
        return True


    victoire_diag2 = True
    for i in range(3):
        if grille[i][2 - i] != symbole:
            victoire_diag2 = False
    if victoire_diag2:
        return True

    return False


def grille_complete(grille):
    for ligne in grille:
        for case in ligne:
            if case == " ":
                return False
    return True


def verifier_resultat(grille):

    if verifier_victoire(grille, "X"):
        return True
    if verifier_victoire(grille, "O"):
        return True
    if grille_complete(grille):
        return True  # Match nul
    return False  # La partie continue


def coup_maitre(grille, symbole):
    """Détermine le coup du maître ('O') en priorité pour gagner, bloquer ou jouer aléatoirement."""
    # Vérifier pour gagner ou bloquer
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    return (i, j)  # Le maître fait un coup gagnant
                grille[i][j] = " "

    # Vérifier si le joueur peut gagner et bloquer
    if symbole == "O":
        adversaire = "X"
    else:
        adversaire = "O"
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = adversaire
                if verifier_victoire(grille, adversaire):
                    grille[i][j] = symbole  # Bloquer le coup gagnant
                    return (i, j)
                grille[i][j] = " "

    # Si aucun coup stratégique n'est nécessaire, jouer au hasard
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return (i, j)


def est_entier(valeur):
    """Vérifie si la valeur peut être convertie en entier."""
    return valeur.isnumeric()

def tour_joueur(grille):
    """Permet au joueur 'X' de choisir une case pour son coup."""
    valide = False  # Nous initialisons la condition de validité à False

    while not valide:  # La boucle continue tant que la condition est False
        # Demander les coordonnées entre 1 et 3
        entree = input("Entrez les coordonnées (ligne, colonne) pour votre coup (entre 1 et 3) : ")

        # Diviser l'entrée en parties
        coordonnees = entree.split()

        # Vérifier que l'entrée contient exactement deux parties
        if len(coordonnees) != 2:
            print("Coordonnées invalides. Veuillez entrer deux nombres séparés par un espace.")
        else:
            ligne, colonne = coordonnees

            # Vérifier si les coordonnées peuvent être converties en entiers

            ligne = int(ligne)  # Convertir la ligne en entier
            colonne = int(colonne)  # Convertir la colonne en entier

            if ligne== str(ligne) or colonne ==str(colonne):
                print("Erreur. Veuillez entrez deux chiffres entre 1 et 3")

            # Vérifier si les coordonnées sont dans la plage [1, 3]
            if ligne < 1 or ligne > 3 or colonne < 1 or colonne > 3:
                print("Les coordonnées doivent être entre 1 et 3. Essayez à nouveau.")
            else:
                # Convertir les coordonnées pour accéder à la grille (de 1-3 à 0-2)
                ligne -= 1
                colonne -= 1

                # Vérifier si la case est vide
                if grille[ligne][colonne] == " ":
                    grille[ligne][colonne] = "X"  # Placer le symbole 'X'
                    valide = True  # Une fois le coup valide, nous mettons valide à True pour sortir de la boucle
                else:
                    print("Cette case est déjà occupée. Essayez une autre.")

def tour_maitre(grille):
    """Permet au maître 'O' de jouer son coup."""
    print("Coup du maître (O) :")
    ligne, colonne = coup_maitre(grille, "O")
    grille[ligne][colonne] = "O"


def jeu_tictactoe():
    """Orchestre le jeu du Tic-Tac-Toe entre un joueur et le maître."""
    grille = [[" " for _ in range(3)] for _ in range(3)]  # Initialisation de la grille vide
    afficher_grille(grille)

    while True:
        # Tour du joueur
        tour_joueur(grille)
        afficher_grille(grille)
        if verifier_resultat(grille):
            print("Le joueur 'X' a gagné !" if verifier_victoire(grille, "X") else "Match nul !")
            return True  # Retourne True si 'X' a gagné ou match nul

        # Tour du maître
        tour_maitre(grille)
        afficher_grille(grille)
        if verifier_resultat(grille):
            print("Le maître du jeu 'O' a gagné !" if verifier_victoire(grille, "O") else "Match nul !")
            return False  # Retourne False si 'O' a gagné ou match nul

