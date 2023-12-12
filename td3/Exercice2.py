"""
Algorithme Operation
Variables N, produit, somme, moyenne,i

Ecrire("Saisir le nombre de valeurs: ")
lire(N)
pour i allant de 1 à N Faire
   Ecrire("Ecrire le", i, "nombre")
"""
num = int(input("Combien de nombre: "))
i = 0 
somme = 0
produit = 1
while (i < num):
    n=int(input("Ecrire un nombre: "))
    somme = somme + n
    produit = produit * n
    i = i + 1
moyenne = somme/num
print("La somme des nombre est ", somme,"\n","Le produit des nombres est",produit,"\n","Le moyenne des nombres est",moyenne)



    
