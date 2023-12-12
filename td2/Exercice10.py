from math import sqrt
"""
Algorithme EquationSecondDgree
Variable a,b,c, delta : Entier
Début
Ecrire("Entrer le 1er nombre entier: ")
Ecrire("Entrer le 2eme nombre entier: ")
Ecrire("Entrer le 3eme nombre entier: ")
lire(a,b,c)
delta <- b^2 - 4*a*c
si (delta =0) alors 
    Ecrire("L'équation admet un solution: x=",-b/2*a)
si (delta >0) alors 
    Ecrire("L'équation admet deux solution: x1=",(-b+(delta)^1/2)/(2*a)," et x2=",(-b+(delta)^1/2)/2*a))
si sinon:
    Ecrire("L'équation n'admet aucun solution")
finsi
fin
"""
a = int(input("Entrer le coefficient a entier: "))
b = int(input("Entrer le coefficient b entier: "))
c = int(input("Entrer le coefficient c entier: "))
delta = (b**2) - (4*a*c)
if (delta == 0) : 
    print("L'équation admet un solution: x=",float(-b/2*a))
elif (delta > 0) :
    print("L'équation admet deux solution: x1=",(-b)+sqrt(delta)/(2*a),"et x2=",((-b)-sqrt(delta)/(2*a)))
else :
    print("L'équation n'admet aucun solution")

