val1 = float(input("Veuillez entrer une première valeur : "))
val2 = float(input("Veuillez entrer une deuxième valeur : "))

if val1 < val2:
    resultat = val2 - val1
else:
    resultat = val1 - val2

print("La différence est de", resultat)