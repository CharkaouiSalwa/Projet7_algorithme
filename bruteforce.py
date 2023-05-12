import itertools

actions = [
    {"Action": 1, "cout": 20, "benefice": 0.05},
    {"Action": 2, "cout": 30, "benefice": 0.1},
    {"Action": 3, "cout": 50, "benefice": 0.15},
    {"Action": 4, "cout": 70, "benefice": 0.2},
    {"Action": 5, "cout": 60, "benefice": 0.17},
    {"Action": 6, "cout": 80, "benefice": 0.25},
    {"Action": 7, "cout": 22, "benefice": 0.07},
    {"Action": 8, "cout": 26, "benefice": 0.11},
    {"Action": 9, "cout": 48, "benefice": 0.13},
    {"Action": 10, "cout": 34, "benefice": 0.27},
    {"Action": 11, "cout": 42, "benefice": 0.17},
    {"Action": 12, "cout": 110, "benefice": 0.09},
    {"Action": 13, "cout": 38, "benefice": 0.23},
    {"Action": 14, "cout": 14, "benefice": 0.01},
    {"Action": 15, "cout": 18, "benefice": 0.03},
    {"Action": 16, "cout": 8, "benefice": 0.08},
    {"Action": 17, "cout": 4, "benefice": 0.12},
    {"Action": 18, "cout": 10, "benefice": 0.14},
    {"Action": 19, "cout": 24, "benefice": 0.21},
    {"Action": 20, "cout": 114, "benefice": 0.18}
]
max_cout = 500
def brute_force(actions, max_cout):
    max_benefice = 0
    meilleure_combinaison = []
    meilleur_cout = 0
    # Générer toutes les combinaisons possibles d'actions
    for i in range(1, len(actions) + 1):
        combinations = itertools.combinations(actions, i)
        # Parcourir toutes les combinaisons
        for combination in combinations:
            # print(combination) pour avoir tous les combinaisons possible des actions
            total_cout = sum(action['cout'] for action in combination)
            # Vérifier si le coût total est inférieur ou égal au budget maximum
            if total_cout <= max_cout:
                total_ben = sum(action['cout'] * action['benefice'] for action in combination)
                # Vérifier si le bénéfice total de la combinaison est meilleur que la meilleure combinaison actuelle
                if total_ben > max_benefice:
                    max_benefice = total_ben
                    meilleure_combinaison = combination
                    meilleur_cout = total_cout
    # Retourner la meilleure combinaison et son bénéfice total
    return (meilleure_combinaison, max_benefice, meilleur_cout)

meilleure_combinaison, max_benefice,meilleur_cout = brute_force(actions, max_cout)
print(f"La meilleure combinaison est : {meilleure_combinaison}")
print(f"Le bénéfice total de la meilleure combinaison est : {max_benefice}")
print(f"le total cout :  {meilleur_cout}")




