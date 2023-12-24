#Fonction Calcul de la somme de deux nombres entiers
n1_test = 2
n2_test = 4

def Som2Entiers(num1,num2):
    return num1 + num2
Somme = Som2Entiers(n1_test, n2_test)
print("Le somme de",n1_test," et ",n2_test," est : ", Somme)

#Fonction Calcul de la factorielle de N (N !)
num_fact_test = 3
def Factoriel(N):
    fac = 1
    for i in range(1,N):
        fac = fac * (i+1)
    return fac
print("La factoriel de ",num_fact_test," est: ", Factoriel(num_fact_test))

#Procedure Vérifier si un nombre entier A divisé un nombre entier B
A_test = 3
B_test = 6
def Divise(A,B):#si B%A == 0 
    if B % A == 0:
        print(A,"divise",B)
    else:
        print(A,"ne divise pas",B)
Divise(A_test,B_test) 


#Fonction Calcul du quotient et du reste de la division entière de deux nombres entiers A et B
def quotientEtReste(A,B):
    Quotient = A // B
    Reste = A % B
    return Quotient, Reste
Q,R = quotientEtReste(A_test,B_test)
print("Le quotient de",A_test,"divise par",B_test,"est : ", Q, "et le reste est :",R)



#Procedue Vérifier si un caractère donné est une voyelle (voyelles : 'a', 'e', 'i', 'o', 'u', 'y')
carac_test = 'e'
def Voyelle(V):
    if V=='a' or V=='e' or V=='i' or V=='o' or V=='u':
        print("Le caractère ",V," est un voyelle")
    else:
        print("Le caractère ",V," n'est pas un voyelle")
Voyelle(carac_test)


#Fonction Permet de permuter (d’échanger) le contenu de deux variables réelles
folat_test1 = 1.5
folat_test2 = 3.7
def Permutation(x, y):
    x , y = y , x
    return x , y
folat_permute = Permutation(folat_test1, folat_test2)
print("Les nouvelles valeurs des variables sont : ", folat_permute[0]," et ", folat_permute[1])


#calcule la valeur absolue A1
A1_test = -6
def Valeur_absolue(val_abs):
    if val_abs < 0:
        return -val_abs
    else:
        return val_abs
print("La valeur absolue de A est: ",Valeur_absolue(A1_test))





















































































































































































































































































































































































































































































