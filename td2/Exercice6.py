"""Algorithme estBissextile
Variables A : Entier
Début
Ecrire("Entrer 1er nombre entier")
lire(A)
# est A divisible par 4 : 
si (A // 4)* 4 <> A ou ((A // 100)* 100 = A et (A // 400)* 400 <> A) alors
   Ecrire("L'année n'est pas bissextile")
sinon:
   Ecrire("L'année est bissextile")
fin si
fin
"""
A = int(input("Entrer l'année: "))
if (A % 4 != 0) or (A % 100 == 0 and (A // 400)* 400 != A):
   print("L'année ",A, "n'est pas bissextile")
else:
   print("L'année ",A," est bissextile")

  

