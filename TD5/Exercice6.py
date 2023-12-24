list = []
#Création d'une fonction qui lire la liste list...
def list_tricks():
   while True:
      nbr_ajout = int(input("Entrer un nombre à la liste : "))
      if nbr_ajout == -1:
         break
      else:
         list.append(nbr_ajout)
   count = 0
   pourc = 0
   for element in list:
      if element % 2 == 0:
         count = count + 1
         pourc = (count * 100)/len(list)
   print("Le nombre des nombre pair est : ",count, " et leur poucentage est : ", pourc,"%")
   print("list= ",list)
list_tricks()

        

        
        
        