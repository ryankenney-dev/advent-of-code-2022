import day1.day1_part2 as day1_part2
import unittest

class TestDay1Part1(unittest.TestCase):

    def test_main(self):

        # Setup
        # ----
        message: str ='''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        expected_sum: int = 45000
        
        # Execute
        # ----
        elves_with_calorie_items: day1_part2.ElvesWithCalorieItems = day1_part2.parse_input(message)

        # Verify
        # ----
        self.assertEqual(day1_part2.get_sum_of_calories_of_top_three_elves(elves_with_calorie_items), expected_sum)
