i = 0 
N = 0
M = 0
som = 0
print("La somme des nombres impair:")
N = int(input("Saisie le début des nombres: "))
M = int(input("Saisie la fin des nombres: "))
for i in range(N,M):
    if i % 2 != 0:
        som = som + i
        i = i + 1
print(som)
