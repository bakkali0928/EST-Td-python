reponse = 0
while True:
    reponse = float(input("Entrer un nombre compris entre 10 et 20: "))
    if reponse > 20:
        print("Plus grand ! ")
    elif reponse < 10:
        print("Plus petit!")
    else:
        print("Convenable! ")
        break