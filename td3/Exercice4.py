N = 0 
i = 0
som = 0
while som < 100:
    N = int(input("Entrer le nombre"+str(i+1)+" : "))
    som = som + N
    i = i + 1
print("La somme des nombres saisis est: ", som,"\n et le nombre d'entiers saisis est: ", i)
