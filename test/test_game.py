import unittest
from game.game import GameModel

class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.words = ['pling', 'släkt', 'kropp', 'kupar']
        self.model = GameModel(self.words)
        self.model.target_word = 'kupar'
        return super().setUp()
    
    def test_valid_words(self):
        self.assertTrue(self.model.valid_word('pling'))
        self.assertTrue(self.model.valid_word('släkt'))
        self.assertTrue(self.model.valid_word('kropp'))
        self.assertTrue(self.model.valid_word('kupar'))
        self.assertFalse(self.model.valid_word('start'))
    
    def test_check_word(self):
        pling_checks = [1, 0, 0, 0, 0]
        släkt_checks = [0, 0, 0, 1, 0]
        kropp_checks = [2, 1, 0, 1, 0]
        kupar_checks = [2, 2, 2, 2, 2]
        self.assertEqual(self.model.check_word('pling'), pling_checks)
        self.assertEqual(self.model.check_word('släkt'), släkt_checks)
        self.assertEqual(self.model.check_word('kropp'), kropp_checks)
        self.assertEqual(self.model.check_word('kupar'), kupar_checks)

    def test_play(self):
        self.model.play('pling')
        self.assertTrue(self.model.tries_left())
        self.model.play('släkt')
        self.assertTrue(self.model.tries_left())
        self.assertFalse(self.model.has_won())
        self.model.play('kropp')
        self.model.play('kupar')
        self.assertTrue(self.model.has_won())
        self.model.max_tries = 4
        self.assertFalse(self.model.tries_left())

    def test_reset(self):
        self.model.reset()
        self.assertFalse(self.model.has_won())
        self.assertTrue(self.model.tries_left())