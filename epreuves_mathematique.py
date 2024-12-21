import random
def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

def epreuve_math_factorielle():
    n=random.randint(1,10)
    print(n)
    fact=int(input("Résultat de votre calcul du factorielle:"))
    result=factorielle(n)
    print(result,fact)
    if fact==result:
        return True
    else:
        return False


def resoudre_equation_lineaire():
    import random
    a=random.randint(1,10)
    b=random.randint(1,10)
    x=-b/a
    return a,b,x

def epreuve_math_equation():
    r,y,z=resoudre_equation_lineaire()
    print("Résoudre l'équation ",{r},"x+",{y}, "=0")
    f=float(input("Quel est la valeur de x:"))
    if f==z:
        return True
    else:
        return False
