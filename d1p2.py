from typing import List
import copy

ElvesWithCalorieItems = List[List[int]]

def parse_input(message: str) -> ElvesWithCalorieItems:
    # parse string into lines
    lines = message.splitlines()

    # group strings by empty string
    groups = []
    group = []
    for line in lines:
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)

    # convert groups of strings to integers
    elves_with_calorie_items = []
    for group in groups:
        calorie_items = []
        for line in group:
            calorie_items.append(int(line))
        elves_with_calorie_items.append(calorie_items)

    return elves_with_calorie_items

def get_sum_of_calories_of_top_three_elves(elves: ElvesWithCalorieItems) -> int:

    # sum calories per elve
    calories_per_elve = []
    for elve in elves:
        calories_per_elve.append(sum(elve))

    # get sum of top three calories per elf
    sorted_calories_per_elve = sorted(calories_per_elve, reverse=True)
    return sum(sorted_calories_per_elve[0:3])
