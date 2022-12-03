import d1p1, d1p2, d2p1, d2p2, d3p1
import argparse
from typing import Any, Callable, Dict, List, Tuple

# A version of argparse.ArgumentParser, that report errors
# with a non-zero exit code
class WrappedArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(125, "%s: error: %s\n" % (self.prog, message))

def read_file(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()

def parse_args_or_exit() -> Any:
    parser = WrappedArgumentParser(description='Runs advent of code solutions.')

    parser.add_argument("-p", "--puzzle", type=str, required=True,
                        help='The puzzle to run. For example "d1p1" or "all" to run all.')
    return parser.parse_args()

def main():
    config: Any = parse_args_or_exit()
    
    day_funcs: Dict[str, Callable[[], None]] = {
        "d1p1": lambda : d1p1.get_max_calories_for_one_elf(d1p1.parse_input(read_file("d1input.txt"))),
        "d1p2": lambda : d1p2.get_sum_of_calories_of_top_three_elves(d1p2.parse_input(read_file("d1input.txt"))),
        "d2p1": lambda : d2p1.compute_answer(d2p1.parse_input(read_file("d2input.txt"))),
        "d2p2": lambda : d2p2.compute_answer(d2p2.parse_input(read_file("d2input.txt"))),
        "d3p1": lambda : d3p1.compute_answer(d3p1.parse_input(read_file("d3input.txt"))),
    }
    
    if config.puzzle == 'all':
        for k in day_funcs.keys():
            print("=== %s ===" % k)
            print("%s" % day_funcs[k]())
    else:
        print("=== config.puzzle ===")
        print("%s" % day_funcs[config.puzzle]())

main()
