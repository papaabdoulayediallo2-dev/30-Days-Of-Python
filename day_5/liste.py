liste_vide = []
liste_plus5 = [
    "orange",
    "banane",
    "mangue",
    "prume",
    "fraises",
    "figue"
]

print(len(liste_plus5))

print(liste_plus5[0])
print(liste_plus5[(len(liste_plus5) // 2) ])
print(liste_plus5[-1])

mixed_data_types = [
    "PAD",
    20,
    1.85,
    False,
    "Malika"
]

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print(it_companies)
print(it_companies[0])
print(it_companies[(len(it_companies) // 2) ])
print(it_companies[-1])


it_companies[0] = "meta"
print(it_companies)
it_companies.append("MAHABAGROUP")
print(it_companies)
milieu = len(it_companies) // 2
it_companies.insert(milieu, "NVIDIA")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

resultat = "#; ".join(it_companies)
print(resultat)

print("Google" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])
print(it_companies[-3:])

it_companies.pop(0)
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

full_stack = front_end + back_end

position_redux = full_stack.index("Redux")

full_stack.insert(position_redux + 1, "Python")
full_stack.insert(position_redux + 2, "SQL")

print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Trier la liste
ages.sort()
print("Liste triée :", ages)

# Trouver l'âge minimum
print("Âge minimum :", min(ages))

# Trouver l'âge maximum
print("Âge maximum :", max(ages))

# Trouver la médiane
n = len(ages)

# Trouver la moyenne
moyenne = sum(ages) / len(ages)
print("Moyenne :", moyenne)
