#fonction qui retourne Vrai si le caractère passé en paramètre est égal à 'o' ou 'O'
def Est_Caractere_O(caractere):
    if caractere.upper() == 'O':
        return True
    return False


#d’afficher la table de multiplication de 1 à 9 d’un nombre entier positif
def TableMulti(nombreEntier):
    for i in range (1,11):
        print(nombreEntier," x ",i," = ", nombreEntier * i,"\n")


#

def Autre_table():
    reponse = input("Voulez-vous afficher la table d'un autre entier ?(Oui : o/O) ")
    return Est_Caractere_O(reponse)


while True:
    nbr_test = int(input("Saisie un nombre entier : "))
    print("La table de multiplication de ", nbr_test, "est : ")
    TableMulti(nbr_test)
    tab_suivant = Autre_table()
    if tab_suivant == False:
       break







    
