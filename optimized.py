import csv

def get_actions_from_csv(filename):
    liste_donnees = []
    with open(filename, newline='') as csvfile:
        lire_csv = csv.DictReader(csvfile, delimiter=',')
        for ligne in lire_csv:
            ligne['price'] = float(ligne['price'])
            ligne['profit'] = float(ligne['profit'])
            liste_donnees.append(ligne)
    return liste_donnees

def top_combinaison(actions, max_cout):
    actions_triees = sorted(actions, key=lambda action: action['profit'], reverse=True)
    meilleure_combinaison = []
    total_cout = 0
    total_benefice = 0

    for action in actions_triees:
        if total_cout + action['price'] <= max_cout:
            meilleure_combinaison.append(action)
            total_cout += action['price']
            total_benefice += action['profit']
        else:
            break

    return meilleure_combinaison, total_benefice, total_cout

filename = 'datatest.csv'
actions_extraites = get_actions_from_csv(filename)
max_cout = 500

meilleure_combinaison, max_benefice, meilleur_cout = top_combinaison(actions_extraites, max_cout)

print(f"La meilleure combinaison est : {meilleure_combinaison}")
print(f"Le bénéfice total de la meilleure combinaison est : {max_benefice}")
print(f"Le coût total de la meilleure combinaison est : {meilleur_cout}")
