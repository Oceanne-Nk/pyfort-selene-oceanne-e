# Exercice 3.1.1 : Epreuve de la Facorielle (faible)

# Cette épreuve génère un nombre aléatoire n, demande au joueur de calculer n!, puis compare sa réponse à la solution correcte et renvoie True si la réponse est correcte, sinon False.

# Débutons cette épreuve. Nous devons tout d'abord implémenter une fonction qui calcule la factorielle de n
import random
def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

# Par la suite, nous devons implémenter une fonction qui génère un nombre aléatoire n entre 1 et 10, puis demande au joueur de calculer la factorielle de n
def epreuve_math_factorielle():
    n=random.randint(1,10)
    print("Épreuve de Mathématiques: Calculer la factorielle de {}.".format(n))

    fact=int(input("Votre réponse: "))

    result=factorielle(n)

# Ici, la réponse du joueur est comparée à la valeur calculée par la fonction factorielle(n). Si la réponse est correcte, un message indiquant que le joueur gagne une clé est affiché, et la fonction renvoie True. Sinon, la fonction renvoie False.
    if fact==result:
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        print("Désolé, la bonne réponse était {}".format(result))
        return False







# Exercice 3.1.2.: Épreuve d'Équation Linéaire (faible)

# Cette épreuve génère deux nombres aléatoires, résout l'équation linéaire ax + b = 0 pour x= -b/a, puis demande au joueur de trouver la valeur de de x et compare sa réponse à la solution correcte.

# Dans cette épreuve, nous devons d'abord implémenter une fonction qui génère deux nombres aléatoires a et b entre 1 et 10, puis résout l'équation linéaire ax + b = 0. Cette fonction renvoie les valeurs de a, b ainsi que la solution correcte de l'équation, c'est-à-dire la valeur de x = -b/a.
def resoudre_equation_lineaire():
    import random
    a=random.randint(1,10)
    b=random.randint(1,10)
    x=-b/a
    return a,b,x

# Pour obtenir les valeurs générées ainsi que la solution, implémentons une fonction qui appelle la précédente. Cette nouvelle foncton demande au joueur de résoudre l'équation et compare la réponse donnée avec la solution correcte. Elle retourne True si la réponse est correcte, sinon False.
def epreuve_math_equation():
    a,b,x=resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation {}x + {} = 0.".format(a,b))
    f=float(input("Quelle est la valeur de x: "))
    if f==x:
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        print("Désolé, la bonne réponse était {}".format(x))
        return False








#Exercice 3.1.4 : Épreuve de la Roulette Mathématique (moyenne)

# Cette épreuve génère cinq nombres aléatoires et applique une opération (addition, soustraction ou multiplication), puis le joueur doit calculer et entrer le résultat pour gagner une clé si sa réponse est correcte.

# Dans cette épreuve, nous devons tout d'abord implémenter une fonction qui génère cinq nombres aléatoires entre 1 et 20, puis choisit aléatoirement une opération parmi l'addition, la soustraction et la multiplication.
def epreuve_roulette_mathematique():
    import random

    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    n3 = random.randint(1,20)
    n4 = random.randint(1,20)
    n5 = random.randint(1,20)

    alea = random.choice(['A','M','S'])

    print("Nombres sur la roulette : [{}, {}, {}, {}, {}]".format(n1,n2,n3,n4,n5))

    if alea=='M':
        result=n1*n2*n3*n4*n5  # Multiplication de tous les nombres
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
    elif alea=='A':
        result=n1+n2+n3+n4+n5   # Addition de tous les nombres
        print("Calculez le résultat en combinant ces nombres avec une addition")
    elif alea=='S':
        result=n1-n2-n3-n4-n5  # Soustraction de tous les nombres dans l'ordre
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
    else:
        print("Erreur. Veuillez entrer un indicatif d'opération correct")
        result = None

    return result

# Ensuite, Le joueur doit calculer le résultat de l'opération appliquée aux nombres de la 'roulette' et fournir sa réponse. S'il donne la bonne réponse, il gagne une clé. La fonction retourne True si la réponse est correcte, sinon elle retourne False.
def epreuve_math_type():
    result=epreuve_roulette_mathematique()  # Nous appelons la fonction de la roulette mathématique

    # Si aucun résultat n'est affiché, cela veut dire qu'il y'a une erreur, donc on s'arrête ici.
    if result is None:
        return False

    n=int(input("Votre réponse : "))

    if n==result:
        print("Bonne réponse ! Vous avez gagné une clé")
        return True
    else:
        print("Désolé, vous avez loupé le résultat. La bonne réponse était {}.".format(result))
        return False



# Exercice 3.1.5 : Fonction epreuve_math() pour la sélection aléatoire d'une épreuve

# Pour finir, la dernière épreuve sélectionne une épreuve parmi plusieurs, l'exécute et retourne le résultat (True ou False) en fonction de la réponse du joueur.

def epreuve_math():
    epreuves = [epreuve_math_type, epreuve_math_factorielle, epreuve_math_equation]

    epreuve = random.choice(epreuves)

    return epreuve()

print(epreuve_math())





