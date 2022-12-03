import day2.day2_part1 as day
import unittest

class TestDay1Part1(unittest.TestCase):

    def test_main(self):

        # Setup
        # ----
        message: str ='''A Y
B X
C Z'''
        expected: int = 15
        
        # Execute
        # ----
        actual: int = day.compute_answer(day.parse_input(message))

        # Verify
        # ----
        self.assertEqual(actual, expected)
