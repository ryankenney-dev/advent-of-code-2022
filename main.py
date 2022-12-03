import day1.day1_part1 as d1p1
import day1.day1_part2 as d1p2
import day2.day2_part1 as d2p1
import day2.day2_part2 as d2p2
import argparse
from typing import Any, Callable, Dict, List, Tuple

# A version of argparse.ArgumentParser, that report errors
# with a non-zero exit code
class WrappedArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(125, "%s: error: %s\n" % (self.prog, message))

def parse_args_or_exit() -> Any:
    parser = WrappedArgumentParser(description='Runs advent of code solutions.')

    parser.add_argument("-p", "--puzzle", type=str, required=True,
                        help='The puzzle to run. For example "d1p1" or "all" to run all.')
    return parser.parse_args()

def d1p1_main() -> None:
    with open("day1/input", 'r') as f:
        message = f.read()
    elves_with_calorie_items: d1p1.ElvesWithCalorieItems = d1p1.parse_input(message)
    max_calories = d1p1.get_max_calories_for_one_elf(elves_with_calorie_items)
    print("max_calories: %s" % max_calories)

def d1p2_main() -> None:
    with open("day1/input", 'r') as f:
        message = f.read()
    elves_with_calorie_items: d1p2.ElvesWithCalorieItems = d1p2.parse_input(message)
    max_calories = d1p2.get_sum_of_calories_of_top_three_elves(elves_with_calorie_items)
    print("max_calories: %s" % max_calories)

def d2p1_main() -> None:
    with open("day2/input", 'r') as f:
        message = f.read()
    inputs: List[Tuple[str, str]] = d2p1.parse_input(message)
    score: int = d2p1.compute_answer(inputs)
    print("score: %s" % score)

def d2p2_main() -> None:
    with open("day2/input", 'r') as f:
        message = f.read()
    inputs: List[Tuple[str, str]] = d2p2.parse_input(message)
    score: int = d2p2.compute_answer(inputs)
    print("score: %s" % score)

def main():
    config: Any = parse_args_or_exit()
    
    day_funcs: Dict[str, Callable[[], None]] = {
        "d1p1": d1p1_main,
        "d1p2": d1p2_main,
        "d2p1": d2p1_main,
        "d2p2": d2p2_main,
    }
    
    if config.puzzle == 'all':
        for k in day_funcs.keys():
            print("=== %s ===" % k)
            day_funcs[k]()
    else:
        print("=== config.puzzle ===")
        day_funcs[config.puzzle]()

main()
