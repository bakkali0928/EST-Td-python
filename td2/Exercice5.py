"""Algorithme Echange
Variables A,B,C,temp : Entiers
Début
Ecrire("Entrer 1er nombre entier")
lire(A)
Ecrire("Entrer 2eme nombre entier ")
lire(B)
Ecrire("Entrer 3eme nombre entier ")
lire(C)
lire(A,B,C)
# Changer A et B : 
si A > B alors
   temp <- A
   A <- B
   B <- temp
fin si
# Changer B et C : 
si B > C alors
   temp <- B
   B <- C
   C <- temp
fin si
# Changer A et B :
si A > B alors
   temp <- A
   A <- B
   B <- temp
fin si
fin
# A = 7 ; B = 0 ; C = 9
A = 0 ; B = 7 ; C = 9
A = 0 ; B = 6 ; C = 9 """

A = int(input("Entrer 1er nombre entier: "))
B = int(input("Entrer 2eme nombre entier: "))
C = int(input("Entrer 3eme nombre entier: "))
if A > B :
   D = A
   A = B
   B = D
if B > C :
   D = B
   B = C
   C = D
if A > B :
   D = A
   A = B
   B = D
print("(val",A,")" "(val",B,")(val",C,")")



