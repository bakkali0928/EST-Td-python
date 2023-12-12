"""
Algorithme estPair
Variable X : Entier
Début
Ecrire("Entrer un nombre entier ")
lire(X)
si (X // 2) * 2 = X alors 
    Ecrire("Le nombre ",X," est pair")
sinon si (X // 2) * 2 = X + 1 alors
    Ecrire("Le nombre ",X," est impair")
finsi
fin

"""
x = int(input("Saisir un nombre entier: "))
if (x // 2) * 2 == x:
    print("Le nombre ",x," est pair")
else:
    print("Le nombre ",x," est impair")

