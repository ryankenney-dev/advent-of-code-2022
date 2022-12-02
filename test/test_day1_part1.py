import day1.day1_part1 as day1_part1
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
        expected_max_calories: int = 24000
        
        # Execute
        # ----
        elves_with_calorie_items: day1_part1.ElvesWithCalorieItems = day1_part1.parse_input(message)

        # Verify
        # ----
        self.assertEqual(day1_part1.get_max_calories_for_one_elf(elves_with_calorie_items), expected_max_calories)
