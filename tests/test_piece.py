import unittest

import gobblet


class PieceTestCase(unittest.TestCase):

    def test_piece(self):
        large = gobblet.Piece('player', 'large', 3)
        large_2 = gobblet.Piece('player two', 'large two', 3)
        small = gobblet.Piece('player', 'small', 1)
        # TODO maybe remove total_ordering on Pieces
        #      could just use the more explicit "a.size > b.size"
        self.assertTrue(large > small)
        self.assertTrue(small < large)
        self.assertTrue(large_2 == large)


if __name__ == '__main__':
    unittest.main()