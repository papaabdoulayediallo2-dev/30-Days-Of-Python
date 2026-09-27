#jour 3 
import math
age = 20
taille = 1.75
complex = 1 + 1j
base = float(input("Entre la base du Triangle"))
hauteur = float(input("Entre la hauteur du Triangle"))
aire_triangle = (base * hauteur) / 2

print(f"L'aire du triangle est {aire_triangle}")

cote_a = float(input("Entrer le cote a du Triangle"))
cote_b = float(input("Entrer le cote b du Triangle"))
cote_c = float(input("Entrer le cote c du Triangle"))

perimetre = cote_a + cote_b + cote_c

print(f"La perimetre du triangle est {perimetre}")

rayon_cercle = float(input("Entrer la rayon du cercle: "))
aire_cercle = 2 * (rayon_cercle ** 2)
circonference_cercle = 2 * rayon_cercle * math.pi

taille_python = len('python')
taille_dragon = len('dragon')
print(len('python') == len('dragon'))
print("on" in "python" and "on" in "dragon")
print("jargon" in "I hope this course is not full of jargon")

print("on" not in "dragon" and "on" not in "python")

longeur_python = len("python")
longeur_python_float = float(longeur_python)
longeur_python_str = str(longeur_python_float)

heure_de_travail = int(input("Entrer le nombre d'heure de travail"))
taux_horaire= int(input("Entrer le taux par heure"))
salaire = heure_de_travail * taux_horaire
print(f"votre salaire est de : {salaire}")

nombre_annee = int(input("entre le nombre d'anne que vous avez vecu (polus simple entre votre age)"))
seconde = nombre_annee * 365 * 24 * 60 * 60

print(f"Vous avez vecu {seconde} seconde")
