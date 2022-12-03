from typing import List, Set, Tuple

# NOTE: Trains equate to packs, and traincars equate to compartments
TrainWithCotents = Tuple[Set[int]]

def char_to_score(char: str) -> int:
    o = ord(char)
    if o >= 97 and o <= 122:
        return o - 96
    if o >= 65 and o <= 90:
        return o - 38
    raise ValueError("Invalid character")

def parse_input(message: str) -> List[TrainWithCotents]:
    # split message into lines and split each line in half
    lines = message.splitlines()

    trains = []
    for line in lines:
        # PROMPT: split string in half
        half = len(line) // 2
        (line[:half], line[half:])
        # PROMPT: convert strings to sets of characters
        sets_of_chars = (set(line[:half]), set(line[half:]))
        # convert sets of characters to sets of scores
        sets_of_scores = (set(map(char_to_score, sets_of_chars[0])), set(map(char_to_score, sets_of_chars[1])))
        trains.append(sets_of_scores)

    return trains

def compute_answer(trains: List[TrainWithCotents]) -> int:

    # PROMPT: for trains, find chars that intersect both touples
    intersections = []
    for train in trains:
        # PROMPT: find intersection of sets
        intersection = train[0].intersection(train[1])
        intersections.extend(intersection)

    return sum(intersections)

