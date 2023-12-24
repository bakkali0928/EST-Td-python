#Écrire un algorithme (en utilisant fonction et/ou procédure) qui permet de calculer le cosinus de
#x € [0, Π/2] sachant que : Cos(W) = 1 – P(W, 2)/2! + P(W,4)/4! – P(W,6)/6! …
import math
def puissance(x,n):
    if n==0:
        return 1
    else:
        return x**n
def factorielle(N):
    fac = 1
    for i in range(1,N):
        fac = fac * (i+1)
    return fac
def cosinus(x,approxi):
    som = 1
    signe = 0
    equation = 0
    for i in range(1,approxi +1):
        signe = (-1)**i
        equation= puissance(x,2*i)/factorielle(2*i)
        som = som + signe * equation
    return som

def affichage():
    x=float(input("Saisie le nombre x dans l'intervalle [0;pi/2]: "))
    while not 0 <= x <= math.pi/2:
        x=float(input("Essayer de saisir un nombre dans l'intervalle [0;pi/2]: "))
    approxi = int(input("Combien des nombres vous voulez approximer le resultat? "))
    cos_x = cosinus(x,approxi)
    print("Le cosinus de ", x, " est :",cos_x)
    return cos_x
affichage()




