import random

def guess_number(secret, guess):
    """
    Compare la devinette au nombre secret.
    Retourne un indice pour guider le joueur.
    """
    if guess < secret:
        return "Trop bas"
    elif guess > secret:
        return "Trop haut"
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

# Tests automatisés
def run_tests():
    """
    Tests automatisés pour vérifier la fonction guess_number.
    """
    print("Exécution des tests...")
    try:
        assert guess_number(50, 25) == "Trop bas", "Échec : La réponse aurait dû être 'Trop bas'"
        assert guess_number(50, 75) == "Trop haut", "Échec : La réponse aurait dû être 'Trop haut'"
        assert guess_number(50, 50) == "Correct !", "Échec : La réponse aurait dû être 'Correct !'"
        print("Tous les tests sont passés avec succès !")
    except AssertionError as e:
        print(f"Erreur dans les tests : {e}")

if __name__ == "__main__":
    # Exécution des tests avant le jeu
    run_tests()
    
    # Démarrage du jeu
    print("\n--- Lancement du jeu ---\n")
    play_game()
