import unittest

from game_test.test_data import *


class MyTestCase(unittest.TestCase):
    def test_sort_cards(self):
        self.assertEqual(["CK", "HK", "CQ"], sort_cards(["CK", "CQ", "HK"]))
        self.assertEqual(["HA", "CK", "CQ"], sort_cards(["CK", "CQ", "HA"]))
        self.assertEqual(["SQ", "CQ", "HQ"], sort_cards(["SQ", "CQ", "HQ"]))
        self.assertEqual(["HQ", "C7", "S2"], sort_cards(["S2", "C7", "HQ"]))
        self.assertEqual(["SK", "SQ", "S7", "S6", "S2"], sort_cards(["S2", "S7", "SQ", "S6", "SK"]))  # FLUSH

    def test_top_raw_scoring(self):
        self.assertEqual(8, scoring_top_raw(["CK", "CQ", "HK"]))
        self.assertEqual(7, scoring_top_raw(["CK", "CQ", "HQ"]))
        self.assertEqual(0, scoring_top_raw(["CK", "CQ", "HA"]))
        self.assertEqual(20, scoring_top_raw(["SQ", "CQ", "HQ"]))
        self.assertEqual(0, scoring_top_raw(["S2", "C7", "HQ"]))
        self.assertEqual(21, scoring_top_raw(["SK", "CK", "HK"]))

    def test_middle_raw_scoring(self):
        self.assertEqual(8, scoring_middle_raw(["S2", "S7", "SQ", "S6", "SK"]))  # FLUSH
        self.assertEqual(50, scoring_middle_raw(["CK", "CQ", "CA", "CT", "CJ"])) # ROYAL FLUSH
        self.assertEqual(30, scoring_middle_raw(["CJ", "CQ", "CT", "C9", "C8"])) # STRAIGHT FLUSH
        self.assertEqual(4, scoring_middle_raw(["CK", "CQ", "HA", "DJ", "ST"])) # STRAIGHT
        self.assertEqual(20, scoring_middle_raw(["SQ", "CQ", "HQ", "DQ", "S8"])) # FOUR OF A KIND
        self.assertEqual(20, scoring_middle_raw(["S8", "SQ", "CQ", "HQ", "DQ"])) # FOUR OF A KIND
        self.assertEqual(12, scoring_middle_raw(["SK", "CK", "HK", "H5", "S5"])) # FULL HOUSE
        self.assertEqual(2, scoring_middle_raw(["S4", "CK", "H5", "HK", "SK"]))  # THREE OF A KIND
        self.assertEqual(0, scoring_middle_raw(["SK", "CQ", "HK", "H5", "S5"])) # FULL HOUSE

    def test_royal_flush(self):
        self.assertEqual(True, is_royal_flush(["SA", "SK", "SQ", "SJ", "ST"]))
        self.assertEqual(False, is_royal_flush(["HA", "SK", "SQ", "SJ", "ST"]))
        self.assertEqual(False, is_royal_flush(["S2", "SK", "SQ", "SJ", "ST"]))

    def test_straight_flush(self):
        self.assertEqual(True, is_straight_flush(["S9", "SK", "SQ", "SJ", "ST"]))
        self.assertEqual(True, is_straight_flush(["SA", "S2", "S3", "S4", "S5"]))
        self.assertEqual(False, is_straight_flush(["HA", "S2", "S3", "S4", "S5"]))
        self.assertEqual(False, is_straight_flush(["SA", "S2", "S7", "S4", "S5"]))

    def test_four_of_a_kind(self):
        self.assertEqual(True, is_four_of_a_kind(["SQ", "CQ", "HQ", "DQ", "S8"]))
        self.assertEqual(True, is_four_of_a_kind(["S8", "SQ", "CQ", "HQ", "DQ"]))
        self.assertEqual(False, is_four_of_a_kind(["S8", "SJ", "CQ", "HQ", "DQ"]))

    def test_full_hoouse(self):
        self.assertEqual(True, is_full_house(["SQ", "CQ", "HQ", "D8", "S8"]))
        self.assertEqual(True, is_full_house(["S8", "SQ", "CQ", "H8", "DQ"]))
        self.assertEqual(True, is_full_house(["S8", "SQ", "C8", "H8", "DQ"]))
        self.assertEqual(False, is_full_house(["S8", "SJ", "CQ", "HQ", "DQ"]))
        self.assertEqual(False, is_full_house(["S8", "SJ", "C8", "HQ", "DQ"]))

    def test_flush(self):
        self.assertEqual(True, is_flush(["SQ", "S7", "SJ", "S2", "S8"]))
        self.assertEqual(True, is_flush(["C8", "CQ", "C6", "C3", "CA"]))
        self.assertEqual(False, is_flush(["S8", "SJ", "CQ", "HQ", "DQ"]))
        self.assertEqual(False, is_flush(["S8", "SJ", "C8", "HQ", "DQ"]))

    def test_straight(self):
        self.assertEqual(False, is_straight(["S9", "SK", "SQ", "SJ", "ST"]))
        self.assertEqual(True, is_straight(["CA", "S2", "S3", "S4", "S5"]))
        self.assertEqual(True, is_straight(["HA", "S2", "S3", "S4", "S5"]))
        self.assertEqual(False, is_straight(["SA", "S2", "C7", "H4", "S5"]))

    def test_three_of_a_kind(self):
        self.assertEqual(True, is_three_of_a_kind(["SQ", "CQ", "HQ", "D7", "S8"]))
        self.assertEqual(True, is_three_of_a_kind(["S8", "SQ", "CQ", "H3", "DQ"]))
        self.assertEqual(True, is_three_of_a_kind(["S8", "SJ", "C8", "H8", "DQ"]))
        self.assertEqual(False, is_three_of_a_kind(["S8", "SJ", "CJ", "HQ", "DQ"]))
        self.assertEqual(False, is_three_of_a_kind(["S8", "SJ", "C8", "HJ", "DQ"]))

    def test_double_pairs(self):
        self.assertEqual(True, is_double_pairs(["S8", "CQ", "HQ", "D7", "S8"]))
        self.assertEqual(True, is_double_pairs(["S8", "SQ", "C3", "H3", "DQ"]))
        self.assertEqual(True, is_double_pairs(["CJ", "SJ", "C8", "H8", "DQ"]))
        self.assertEqual(False, is_double_pairs(["S8", "SJ", "CT", "HQ", "DQ"]))
        self.assertEqual(False, is_double_pairs(["S8", "SJ", "CT", "HJ", "DQ"]))


if __name__ == '__main__':
    unittest.main()
