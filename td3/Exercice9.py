num = 0
max = 0
i = 0
position = 0
for i in range(1,20):
    num = int(input("Saisie le nombre "+str(i)+": "))
    if num > max :
        max = num
        position = i
print("La plus grande valeur est ",max,"\n la position de ce nombre est:", position)

