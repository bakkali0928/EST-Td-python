"""
Variables i, j, val : Entier Tableau X[1, 2]: Entier
Début
Val ← 1
Pour i ← 0 à 1
    Pour j ← 0 à 2
         X[i, j] ← Val
         Val ← Val + 1
    FinPour 
FinPour
Pour j ← 0 à 2
    Pour i ← 0 à 1
    Écrire X[i, j]
    FinPour 
FinPour
"""
"""
 l’algorithme suivant produit  :
 1 2 3 4 5 6 
"""
val = 1
X = []
#Remplissage de liste
for i in range(2):
    for j in range(3):
        X.append(val)
        val += 1
#Affichage de liste
for element in X:
    print(element, end=" ")
