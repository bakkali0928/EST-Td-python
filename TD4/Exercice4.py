"""
Algorithme ResultatLicenceLMD
variable mat_cherche, i, element : Entier
        est_existe : booléan
Tableau matricule[200] d'entier;
Début 
matricule = [1,68,0764,45789,...] # 200 matricule
Ecrire("Veillez saisie votre matricule: ")
lire(mat_cherche)
est_existe = false
pour i de 1 à 200:
    si mat_cherche = matricule[i] Faire:
       est_existe = True
       Sortir
finPour
si est_existe = false Faire:
   Ecrire("Désole, Vous êtes ajounée! ")
sinon:
   Ecrire("Bravo, Vous êtes admis! ")
Finsi
Fin
"""
#Initialiser 200 matricule aléatoire
import random
matricule = []
for i in range(200):
    nbr_alt = random.randint(1,207)
    matricule.append(nbr_alt)
#L'utilisateur saisie leur matricule
mat_cherche = int(input("Veillez saisie votre matricule: "))
est_existe = False
#Recherche si le matricule est dans le tableau
for i in range(200):
    element = matricule[i]
    if mat_cherche == element:
       est_existe = True
       break
#L'affichage de résultat
if est_existe == False:
   print("Désole, Vous êtes ajounée! ")
else:
   print("Bravo, Vous êtes admis! ")
print(matricule)
