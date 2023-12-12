mot_correct = "1234"
mot_saisie = "0"
while True:
    mot_saisie = input("Saisie le mot de passe: ")
    if mot_saisie != mot_correct:
        print("Mot de passe incorrect! ")
    else:
        break
print("Le mot de passe est correct! ")