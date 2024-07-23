import unittest
from unittest.mock import patch
from app import determine_winner, get_computer_choice, display_final_score

class TestRockPaperScissors(unittest.TestCase):
    def test_determine_winner(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(determine_winner('paper', 'rock'), 'user')
        self.assertEqual(determine_winner('scissors', 'paper'), 'user')
        self.assertEqual(determine_winner('rock', 'paper'), 'computer')
        self.assertEqual(determine_winner('paper', 'scissors'), 'computer')
        self.assertEqual(determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(determine_winner('rock', 'rock'), 'tie')
        self.assertEqual(determine_winner('paper', 'paper'), 'tie')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'tie')

    def test_get_computer_choice(self):
        choices = ['rock', 'paper', 'scissors']
        # Since the choice is random, test it by checking if the returned value is in the expected choices
        self.assertIn(get_computer_choice(choices), choices)

    @patch('builtins.print')
    def test_display_final_score(self, mock_print):
        score = {'user': 2, 'computer': 1}
        rounds_played = 3
        display_final_score(score, rounds_played)
        mock_print.assert_called_with("Final score: User - 2, Computer - 1, Rounds Played - 3")

if __name__ == '__main__':
    unittest.main()