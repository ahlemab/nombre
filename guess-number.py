import random

def guess_number(secret, guess):
    """
    Compare la devinette au nombre secret.
    Retourne un indice pour guider le joueur.
    """
    if guess > secret:
        return "Trop haut !"
    elif guess < secret:
        return "Trop bas !"
    return "Correct !"

def play_game():
    """
    Fonction principale pour jouer au jeu.
    """
    print("Bienvenue dans 'Guess the Number' !")
    print("J'ai choisi un nombre entre 1 et 100. Essayez de le deviner.")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Entrez votre supposition (1-100) : "))
            attempts += 1
            result = guess_number(secret_number, guess)
            print(result)
            if result == "Correct !":
                print(f"Félicitations ! Vous avez trouvé le nombre en {attempts} essais.")
                break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")


if __name__ == "__main__":
      
    # Démarrage du jeu
    print("\n--- Lancement du jeu ---\n")
    play_game()
