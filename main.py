def factorielle(n):
    n=-1
    while n<0:
        n=int(input("Valeur positive"))
    if n==0 or n==1:
        return 1
    else:
        f=1
        for i in range (1,n+1):
            f*=i
        return f
def epreuve_math_factorielle():
    import random
    nombre=random.randint(1,10)
    fact=int(input("Résultat de votre calcul du factorielle"))
    result=factorielle(nombre)
    np="Vous gagnez une clé"
    if fact==result:
        return True, np
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
    print("Résoudre l'équation ",{r},"x+",{y})
    f=float(input("Quel est la valeur de x:"))
    nr="Vous gagnez une clé"
    if f==z:
        return True, nr
    else:
        return False
print(epreuve_math_equation())
