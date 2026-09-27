# Day 2: 30 Days of python programming
import math
prenom = 'Laye'
nom = 'Diallo'
pays = 'Senegal'
ville = 'Malika'
age = 20
annee = 2026
is_married = False
is_true = True
is_light_on = False

a, b = 'lettre1', 'lettre2'

print(type(prenom))
print(type(nom))
print(type(pays))
print(type(age))
print(type(annee))
print(type(is_married))
print(type(is_light_on))
print(prenom)
print('Longueur du prenom :', len(prenom))
print('Longueur du prenom :', len(nom))
num_one = 5
num_two = 4
rayon = 30
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

area_of_circle = math.pi * (rayon**2)

rayon_utilisateur = float(input("Entre le rayon: "))
aire = math.pi * (rayon_utilisateur**2)

print("L'aire du cercle est :", aire)
