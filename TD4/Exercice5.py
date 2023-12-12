"""
Algorithme TemFevrier2013
variable jours_froid, jours_chaud, i : Entiers
Tableau tempf[29] d'entier;
Début 
tempf = [1,12,34,12,-13,0,-1,8,23,-4,6,-2,0,5,14,36,12,14,11,-10,7,-1,2,0,14,25,12,6,-2 # 28 jours
jours_chaud = 0
jours_froid = 0
pour i de 1 à 28:
    si tempf[i] >= jours_chaud Faire:
       jours_chaud = jours_chaud + 1
    si tempf[i] <= jours_froid Faire:
       jours_froid = jours_froid + 1
finPour
Ecrire("Nombre de jours chauds (≥10°): ",jours_chauds," Nombre de jours froids (<10°) : ,jours_froids)
Fin
"""
import random
tempf = []
for i in range(28):
    nbr_alt = random.randint(-55,55)
    tempf.append(nbr_alt)
jours_chaud = 0
jours_froid = 0
for i in range(28):
    if tempf[i] >= jours_chaud:
       jours_chaud = jours_chaud + 1
    if tempf[i] <= jours_froid:
       jours_froid = jours_froid + 1
print("Le vecteur de température de Février 2013 est: ", tempf)
print("Nombre de jours chauds (≥10°): ",jours_chaud," Nombre de jours froids (<10°) : ",jours_froid)
