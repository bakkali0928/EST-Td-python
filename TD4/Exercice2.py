"""
variables i, j, input : Entier
Tableau list(10) : Entier
Début
#Remplissage list
Pour i de 1 à 10 Faire:
    Ecrire("Saisie le nombre ",i,": ")
    lire(input)
    list(i) <-- input
FinPour
#Affichage list
pour i de 1 à 10 Faire:
    Ecrire(list(i))
FinPour
Fin
"""
i = 1
list = []
for i in range(1,11):
    saisie = int(input("Saisie le nombre "+str(i)+" : "))
    list.append(saisie)
for saisie in list:
    print(saisie, end=" ")


    
