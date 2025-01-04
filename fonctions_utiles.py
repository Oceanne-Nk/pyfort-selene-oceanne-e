# FORT BOYARD SIMULATOR : Sélène AKDOGAN et Océanne TSANE :
#Dans le module fonctions_utiles.py, on doitimplémenter plusieurs fonctions qui géreront les joueurs, les épreuves, et l'enregistrement des résultats du jeu. Ces fonctions seront utilisées pour organiser et suivre le déroulement du jeu.

#La fonction introduction() affiche un message de bienvenue et présente le contexte du jeu. Elle informe le joueur de l'objectif principal : obtenir trois clés magiques pour accéder à la salle du trésor. Ce message sert à immerger le joueur dans l'aventure, en le préparant aux épreuves à venir. La fonction ne retourne rien, elle se contente de l'affichage des instructions.
def introduction():
    print("Bienvenue, aventurier !")
    print("Prépare-toi pour un voyage épique où des épreuves t'attendent à chaque coin de rue.")
    print("Ton objectif ? Très simple ! Il te faut TROIS clés magiques pour déverrouiller la fameuse salle du trésor.")
    print("Chaque clé te rapproche de la victoire... et des richesses incroyables !")
    print("C'est parti ! La chasse aux clés commence maintenant. Bonne chance, et que la chance soit avec toi !")




#La fonction composer_equipe() permet de créer une équipe en ajoutant des joueurs à une liste.
def composer_equipe():
    # Liste pour stocker les joueurs
    equipe = []


    nb_joueurs = 0
    while nb_joueurs < 1 or nb_joueurs > 3:
        nb_joueurs = int(input("Combien de joueurs voulez-vous inscrire dans l'équipe ? (max 3) : "))
        if nb_joueurs > 3:
            print("Erreur : L'équipe ne peut comporter que 3 joueurs maximum.")
        elif nb_joueurs < 1:
            print("Erreur : L'équipe doit comporter au moins 1 joueur.")

    # Composition de l'équipe
    for i in range(nb_joueurs):
        print(f"\nJoueur {i + 1} :")

        # Demande des informations pour chaque joueur
        nom = input("Nom du joueur : ")
        profession = input("Profession du joueur : ")
        leader = input("Ce joueur est-il le leader de l'équipe ? (oui/non) : ").strip().lower()

        # Création du joueur sous forme de dictionnaire
        joueur = {
            'nom': nom,
            'profession': profession,
            'leader': leader == 'oui',
            'cles_gagnees': 0
        }

        # Ajout du joueur à l'équipe
        equipe.append(joueur)

    # Vérification si un leader a été désigné
    leader_trouve = False
    for joueur in equipe:
        if joueur['leader']:
            leader_trouve = True

    # Si aucun leader n'a été désigné, le premier joueur devient le leader
    if not leader_trouve:
        print("Aucun leader n'a été désigné. Le premier joueur devient automatiquement le leader.")
        equipe[0]['leader'] = True

    # Retourner la liste des joueurs de l'équipe
    return equipe


#La fonction menu_epreuves() affiche un menu d'options pour choisir une épreuve. Elle présente quatre options à l'utilisateur : mathématiques, logique, hasard et l'énigme du Père Fouras.
def menu_epreuves():
    # Affichage du menu des épreuves
    print("\nChoisissez une épreuve :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du hasard")
    print("4. Énigme du Père Fouras")

    # Demande du choix à l'utilisateur
    choix_valide = False  # Initialisation de la variable
    while not choix_valide:
        choix = int(input("Choix : "))
        if 1 <= choix <= 4:
            choix_valide = True  # Le choix est valide, on sort de la boucle
        else:
            print("Erreur, vous devez choisir une épreuve entre 1 et 4.")

    # Retourner le choix
    return choix



#La fonction choisir_joueur(equipe) permet à l'utilisateur de choisir un joueur parmi ceux présents dans l'équipe pour participer à une épreuve.
def choisir_joueur(equipe):
    print("\nVoici les joueurs disponibles :")
    for i, joueur in enumerate(equipe):
        print(f"{i + 1}. {joueur['nom']} ({joueur['profession']}) - Leader: {'Oui' if joueur['leader'] else 'Non'}")

    # Demande du choix du joueur
    choix_joueur = int(input("\nChoisir le joueur qui participera à l'épreuve (entrez le numéro attribué) : "))

    # Validation du choix
    while choix_joueur < 1 or choix_joueur > len(equipe):
        choix_joueur = int(input("Erreur : Choisissez un numéro valide de joueur : "))

    return equipe[choix_joueur - 1]


