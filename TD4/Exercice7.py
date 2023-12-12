"""
Algorithme moyenne_note
Variables i, j, l, c,  : Entiers
Tableau matrice[l,c]: Entiers
Début
Ecrire("Saisie le nombres des lignes et des colonnes: ")
Lire(l,c)
pour i <-- 0 à l-1 Faire:
    pour j <-- 0 à c-1 Faire:
        Ecrire("Saisie l'élément ", i+1 ,": ")
        Lire(matrice[i][j])
    FinPour
Finpour
Ecrire("La matrice: ", matrice[l,c])
#Déterminer le plus grand élément et le petit élément ainsi,
#la position de plus grand élément et le petit élément d'une matrice
grand <-- matrice[0,0]
pour chaque element dans matrice:
    si element > grand Faire:
       grand <-- element
       pos_grand <-- [i,j]
    si element > petit Faire:
       petit <-- element
       pos_petit <-- [i,j]
Finpour
Ecrire("Le plus grand élément est a la position ",pos_grand," avec une valeur de ",grand)
Ecrire("Le plus petit élement est a la position ",pos_petit," avec une valeur de ",petit)



    

        



        
      

Fin
"""