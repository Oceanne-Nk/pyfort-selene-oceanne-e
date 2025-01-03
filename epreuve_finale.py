import json
import random

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
salle_De_Tresor("data/indicesSalle.json")