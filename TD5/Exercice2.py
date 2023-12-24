mois_saisie = 2
annee_saisie = 1980
tab_jours31 = [1,3,5,7,8,10,12]
#EstUnMoisDeTrentUn
def EstUnMoisDeTrentUn(mois):
   if mois in tab_jours31:
      return 1
   else:
      return 0
EstUnMoisDeTrentUn(mois_saisie)


#bissextile
annee_saisie = 1980
def Bissextile(annee):
   if annee % 4 == 0 and (annee % 100 != 0 or annee % 4 == 0):
      return 1
   else:
      return 0
Bissextile(annee_saisie)


#fonction retourne le nombres de jours de mois du fonction EstUnMoisDeTrentUn,Et aussi le nombre des jours de l'annee du fonction Bissextile
def NombreJoursAnneeEtMois(mois,annee):
   if EstUnMoisDeTrentUn(mois):
      print("Le nombre des jours de mois est : 31")
   elif mois == 2:
      if Bissextile(annee):
         print("Le nombre des jours du mois est : 29")
      else:
         print("Le nombre des jours du mois est : 28")
   else:
      print("Le nombre des jours du mois est : 30")
   if Bissextile(annee):
      print("Le nombre des jours de l'annee ",annee," est 366")
   else:
      print("Le nombre des jours de l'annee ",annee," est 365")
NombreJoursAnneeEtMois(mois_saisie,annee_saisie)

      





                
             






    
