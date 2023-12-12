"""
Algorithme moyenne_note
Variables i, j, k : Entiers
Tableau notes[30,2]: Réel
        moy[30]: Réel
Début
# notes la liste qui contient tous les notes des élèves
notes = [[12.5,18],[13,15.75],[20,19.75],[15,15],...]#il y a 30 li et 2 col
#Calcul des moyenne, et les arranger dans le tableau moy[30]
pour k <-- 0 à 29 Faire:
    pour i <-- 0 à 29 Faire:
        moyenne <-- (notes[i][0] + notes[i][1])/2
    Finpour
    moy[k] <-- moyenne
Finpour
#L'affichage des moyenne
Ecrire("Les moyenne des élèves sont : ", moy[30])

#La moyenne générale de la classe
som_moy = moy[0]
pour i <-- 1 à 29:
    som_moy = som_moy + moy[i]
moy_gn = som_moy/30
#L'affichage de moyenne générale
Ecrire("Le moyenne générale est: ",moy_gn)
#Comptez les moyennes supérieures à la moyenne de la classe
moy_su = 0
pour chaque element dans moy:
    if element > moy_gn:
        moy_su = moy_su + 1
Ecrire("le nombre des moyennes supérieures à la moyenne de la classe sont: \n",moy_su)
Fin
"""
# notes la liste qui contient tous les notes des élèves
notes = [[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75],[20,19.75],[15,15],[12.5,18],[13,15.75]]
#Calcul des moyenne, et les arranger dans le tableau moy
moy = [0.0] * 30
for i in range(30):
   moyenne = 0.0
   for j in range(2):
        moyenne = moyenne + notes[i][j]
   moy[i] = moyenne / 2
#L'affichage des moyenne
print("Liste des notes de ds1 et ds2: \n",notes)
print("\n")
print("\n")
print("Liste des moyenne: \n",moy)
#La moyenne générale de la classe
som_moy = moy[0]
for i in range(1,29):
    som_moy = som_moy + moy[i]
moy_gn = som_moy/30
#L'affichage de moyenne générale
print("Le moyenne générale est: \n",moy_gn)
#Comptez les moyennes supérieures à la moyenne de la classe
moy_su = 0
for element in moy:
    if element > moy_gn:
        moy_su = moy_su + 1
print("le nombre des moyennes supérieures à la moyenne de la classe sont: \n",moy_su)










