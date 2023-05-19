from bruteforce import brute_force, actions, max_cout


def main():
    meilleure_combinaison, max_benefice = brute_force(actions, max_cout)
    print("Meilleure combinaison :", meilleure_combinaison)
    print("Bénéfice maximum :", max_benefice)

if __name__ == "__main__":
    main()
