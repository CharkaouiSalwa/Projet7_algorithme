import csv


def get_actions_from_csv(filename):
    liste_donnees = []
    with open(filename, newline='') as csvfile:
        lire_csv = csv.DictReader(csvfile, delimiter=',')
        for ligne in lire_csv:
            ligne['price'] = float(ligne['price'])
            ligne['profit'] = float(ligne['profit'])
            if ligne['price'] != 0:
                ligne['gain'] = ligne['profit'] / ligne['price']
                # on multiplie le résultat par 100 pour obtenir le pourcentage
                ligne['gain'] = ligne['gain'] * 100
            else:
                ligne['gain'] = 0
            liste_donnees.append(ligne)
    return liste_donnees


def top_combinaison(actions, max_cout):
    actions_triees = sorted(actions, key=lambda action: action['gain'], reverse=True)
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


# Demander à l'utilisateur de choisir le fichier CSV à traiter
choix = input("Choisissez le fichier à traiter (1 ou 2) : ")
if choix == "1":
    filename = 'datatest.csv'
elif choix == "2":
    filename = 'datatest2.csv'
else:
    print("Choix invalide. Le programme s'arrête.")
    exit()

actions_extraites = get_actions_from_csv(filename)
max_cout = 500

meilleure_combinaison, max_benefice, meilleur_cout = top_combinaison(actions_extraites, max_cout)

print(f"La meilleure combinaison est : {meilleure_combinaison}")
print(f"Le bénéfice total de la meilleure combinaison est : {max_benefice}")
print(f"Le coût total de la meilleure combinaison est : {meilleur_cout}")


# Afficher les données extraites du CSV
#for action in actions_extraites:
   # print(action)