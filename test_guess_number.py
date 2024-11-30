import unittest
from guess_number import check_guess  # Importe la fonction à tester

class TestGuessNumber(unittest.TestCase):
    def test_too_low(self):
        self.assertEqual(check_guess(3, 5), "Trop bas !", "Le test pour 'Trop bas' a échoué.")

    def test_too_high(self):
        self.assertEqual(check_guess(7, 5), "Trop haut !", "Le test pour 'Trop haut' a échoué.")

    def test_correct_guess(self):
        self.assertEqual(check_guess(5, 5), "Correct !", "Le test pour 'Correct' a échoué.")

if __name__ == "__main__":
    unittest.main()