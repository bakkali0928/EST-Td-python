
"""Algorithme LeSigne
Variable a,b, produit, somme: Entier
Début 
Ecrire("Saisir deux nombres entier a et b")
lire(a,b)
si (a>0 et b>0) ou (a<0 et b<0) Alors
    ecrire("Le signe de produit est: +")
sinon:
    ecrire("Le signe de produit est: -")
finsi
si (a<b et b>0) ou (a<0 et b<0)
    ecrire("Le signe du somme est: -")
sinon:
    ecrire("Le signe du somme est: +")*
finsi
"""
a = int(input("Saisir deux nombres entier a: "))
b = int(input("Saisir deux nombres entier b: "))
if (a>0 and b>0) or (a<0 and b<0):
    print("Le signe de produit est: +")
elif (a>0 and b<0) or (a<0 and b>0):
    print("Le signe de produit est: -")
else:
    print("La signe de produit est neutre")

if a<-b or b<-a or (a<0 and b<0):
    print("La somme est négatif")
else:
    print("La somme est positif")





    


