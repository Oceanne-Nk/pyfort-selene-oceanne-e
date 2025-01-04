# FORT BOYARD SIMULATOR : Sélène AKDOGAN et Océanne TSANE :
#Exercice 3.5. Le module epreuve_finale.py
#Le module simule la dernière étape du jeu où l’équipe, après avoir collecté toutes les clés, doit résoudre un code pour accéder à la salle du trésor en utilisant des indices et un mot-code.
import json
import random

#La fonction salle_De_Tresor(fichier) charge les données d'un fichier JSON, choisit aléatoirement une émission et une année, puis demande au joueur de deviner un mot-code en utilisant des indices, avec trois essais pour répondre correctement.
def salle_De_Tresor(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)

    jeu_tv = jeu_tv[list(jeu_tv.keys())[0]]

        # Sélection aléatoire d'une année et d'une émission
    annee = random.choice(list(jeu_tv.keys()))
    emission = random.choice(list(jeu_tv[annee].keys()))

        # Extraire les indices et le mot-code
    donnees = jeu_tv[annee][emission]
    indices = donnees['Indices']
    mot_code = donnees['MOT-CODE'].strip()

        # Afficher les trois premiers indices

    for indice in indices[:3]:
        print("- {}".format(indice))

        # Boucle de jeu
    essais = 3
    reponse_correcte = False
    indices_supplementaires = indices[3:]

    while essais > 0 and not reponse_correcte:
        reponse= input("Entrez le mot-code ({} essais restants) : ".format(essais)).strip()
        if reponse.lower() == mot_code.lower():
            reponse_correcte= True
        else:
            essais -= 1
            if essais > 0:
                print("Incorrect ! Vous avez {} essais restants.".format(essais))
            # Afficher un nouvel indice seulement si on en a encore
                if indices_supplementaires:
                    print("Indice supplémentaire : {}".format(indices_supplementaires[0]))
                    indices_supplementaires = indices_supplementaires[1:]

    if reponse_correcte==False:
        print("Échec ! Le mot-code était : {}".format(mot_code))
        print("Dommage, vous avez échoué. Meilleure chance la prochaine fois !")
    else:
        print("Bravo ! Vous avez trouvé le mot-code et gagné la partie !")




# Exécuter le jeu
