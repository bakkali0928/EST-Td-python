"""Algorithme CalculPrime
Variables CHA,  : Entier 
Début
Ecrire("Saisir le chiffre d'affaire réalisé: ")
lire(CHA)
si CHA <= 150000 alors
   PRA <- 0
sinon si CHA > 150000 et CHA <= 500000 alors
   PRA <- 1
sinon :
   PRA <- 2
finsi
si PRA = 0 alors
   PRC <- CHA * 0
sinon si PRA = 1 alors
   PRC <- CHA * (1/100)
sinon :
   PRC <- CHA * (2/100)
finsi 
Ecrire("le chiffre d'affaires réalisé ",CHA," le pourcentage de prime applicable ",PRA," la prime du commercial ",PRC)

fin
"""
# Code Python de l'algorithme CalculPrime
CHA = int(input("Saisir le chiffre d'affaire réalisé: "))
#Prime applicable
if CHA <= 150000 :
   PRA = 0
elif  CHA > 150000 & CHA <= 500000 :
   PRA = 1
else :
   PRA = 2
#Prime de commercial
if PRA == 0 :
   PRC = CHA * 0
elif PRA == 1 :
   PRC = CHA * (1/100)
else :
   PRC = CHA * (2/100)
print("le chiffre d'affaires réalisé ",CHA," le pourcentage de prime applicable ",PRA,"% la prime du commercial ",PRC,"DH")

