"""Algorithme platReaction
Variables sucre, sal, chaud, cher : booléennes
Début
Ecrire("Est-ce que le plat est sucré ? (Donnez 1 pour oui, et 0 pour non)")
lire(sucre)
Ecrire("Est-ce que le plat est salée ? (Donnez 1 pour oui, et 0 pour non)")
lire(sal)
Ecrire("Est-ce que le plat est  ? (Donnez 1 pour oui, et 0 pour non)")
lire(chaud)
Ecrire("Est-ce que le plat est cher ? (Donnez 1 pour oui, et 0 pour non)")
lire(cher)
si sucre = 1 et sal = 0 et chaud = 0 et cher = 0 alors
   Ecrire("Love")
sinon si sal = 1 et sucre = 0 et chaud = 1 alors
   Ecrire("Haha")
sinon si sal = 0 et sucre = 0 et chaud = 0 alors
   Ecrire("Wow")
sinon si sucre = 1 sal = 1 et chaud = 0 alors
   Ecrire("Sad")
sinon:
   Ecrire("Angry")
finsi 
fin
"""
sucre = int(input("Est-ce que le plat est sucré ? (Donnez 1 pour oui, et 0 pour non: "))
sal = int(input("Est-ce que le plat est salée ? (Donnez 1 pour oui, et 0 pour non: "))
chaud = int(input("Est-ce que le plat est chaud ? (Donnez 1 pour oui, et 0 pour non: "))
cher = int(input("Est-ce que le plat est cher ? (Donnez 1 pour oui, et 0 pour non: "))
if sucre == 1 and sal == 0 and chaud == 0 and cher == 0 :
    print ("Love")
elif sal == 1 and sucre == 0 and chaud == 1 :
    print("Haha")
elif sal == 0 and sucre == 0 and chaud == 0 :
    print("Wow")
elif sucre == 1 and sal == 1 and chaud == 0 :
    print("Sad")
else:
    print("Angry")


