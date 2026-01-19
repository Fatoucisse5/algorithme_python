# on demande le nom et l'age
nom = input("quel est votre nom ? ")
age = input("quel est votre age ? ")
#nom = "fatou"
#age = "20"
print("Vous vous appelez "  + nom + ",vous avez  "+ age +"ans")
age_prochain = int(age) + 1
try:
    age_prochain = int(age) + 1
except: 
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else: 
    print("Vous vous appelez" + nom +",vous avez" + str(age) +"ans")
    print("l'an prochain vous aurez" + str(age_prochain) +"ans")      
