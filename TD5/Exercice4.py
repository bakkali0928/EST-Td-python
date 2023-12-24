#carré parfait si X = i * i
X = 196

def CarreParfait(nombre):
    for i in range(nombre):
        if i * i == nombre:
            return i
    return None

racine_carre = CarreParfait(X)

if racine_carre is not None:
    print("Le nombre", X," est un carré parfait", " et sa racine est: ",racine_carre)
else:
    print("Le nombre", X," n'est pas un carré parfait")
            
