import unittest

from game_test.test_data import scoring_top_raw, scoring_middle_raw


class MyTestCase(unittest.TestCase):
    def test_top_raw_scoring(self):
        self.assertEqual(8, scoring_top_raw({"CK", "CQ", "HK"}))
        self.assertEqual(7, scoring_top_raw({"CK", "CQ", "HQ"}))
        self.assertEqual(0, scoring_top_raw({"CK", "CQ", "HA"}))
        self.assertEqual(20, scoring_top_raw({"SQ", "CQ", "HQ"}))
        self.assertEqual(0, scoring_top_raw({"S2", "C7", "HQ"}))
        self.assertEqual(21, scoring_top_raw({"SK", "CK", "HK"}))

    def test_middle_raw_scoring(self):
        self.assertEqual(8, scoring_middle_raw({"S2", "S7", "SQ", "S6", "SK"}))  # FLUSH
        self.assertEqual(50, scoring_middle_raw({"CK", "CQ", "CA", "CT", "CJ"})) # ROYAL FLUSH
        self.assertEqual(30, scoring_middle_raw({"CJ", "CQ", "CT", "C9", "C8"})) # STRAIGHT FLUSH
        self.assertEqual(4, scoring_middle_raw({"CK", "CQ", "HA", "DJ", "ST"})) # STRAIGHT
        self.assertEqual(20, scoring_middle_raw({"SQ", "CQ", "HQ", "DQ", "S8"})) # FOUR OF A KIND
        self.assertEqual(20, scoring_middle_raw({"S8", "SQ", "CQ", "HQ", "DQ"})) # FOUR OF A KIND
        self.assertEqual(12, scoring_middle_raw({"SK", "CK", "HK", "H5", "S5"})) # FULL HOUSE
        self.assertEqual(2, scoring_middle_raw({"S4", "CK", "H5", "HK", "SK"}))  # THREE OF A KIND
        self.assertEqual(0, scoring_middle_raw({"SK", "CQ", "HK", "H5", "S5"})) # FULL HOUSE



if __name__ == '__main__':
    unittest.main()
