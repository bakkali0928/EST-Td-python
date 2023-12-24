#Écrire une fonction ou procédure qui permet d’avoir un nombre entier positif
# et afficher son image miroir. Exemple le nombre est 3524, on doit afficher 4253.
#Solution 
def miroir(nombre):
    miroir_nbr = int(str(nombre)[::-1])
    return miroir_nbr
nbr_test = int(input("Saisie un nbr : "))
resultat = miroir(nbr_test)
print("L'image miroire de ",nbr_test, " est : ", resultat)



