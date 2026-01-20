"""
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

#la boucle while
n = 0 # cree la variable 
while n < 10:
    print ("Valeur de n: " + str(n))
    n = n + 1
    
print("fin de la boucle")
mot_de_passe = ""
while not mot_de_passe == "TOTO":
    mot_de_passe = input("quel est le mot de passe ? ")
print("mot de passe correct, vous avez acces au compte")


nom = input("quel est votre nom ? ")

age = 0
while age == 0:
    age_str =input("quel est votre age ? ")
    try: 
        age = int(age_str)
    except:
        print("ERREUR : Vous devez rentrer un nombre pour l'age")
print("Vous vous appelez" + nom +",vous avez" + str(age) + "ans")
print("l'an prochain vous aurez" + str(age +1) + "ans")

#exercice
#demander le nom
nom = ""
while nom == "":
    nom = input("entrer votre nom")
    

def demander_age ():
    age_int = 0
    while age_int == 0:
        age_str = input("quel est votre age ? ")
        try: 
            age_int = int(age_str)
        except:
            print("ERREUR : Vous devez rentrer un nombre pour l'age")
    return age_int

#demander le nom
nom = ""
while nom == "":
    nom = input("entrer votre nom")

#demander l'age
age = demander_age ()

#afficher les resultats
print("Vous vous appelez" + nom +",vous avez" + str(age) + "ans")
print("l'an prochain vous aurez" + str(age +1) + "ans")
"""

"""
#exercice
def demander_nom() :
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("quel est votre nom ? ")
    return reponse_nom
"""    
#exercice
age =input("entrer un age")
if age == 17:
 print ("vous etes presque majeur")
elif age == 18:
 print("tout juste majeur;FELICITATIONS")
else:
 print("vous etes majeur")