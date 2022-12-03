from typing import List, Tuple

map_my_input_to_choice = {
    "X": "cat",
    "Y": "bird",
    "Z": "worm",
}

map_my_choice_to_score = {
    "cat": 1,
    "bird": 2,
    "worm": 3,
}

map_their_input_to_choice = {
    "A": "cat",
    "B": "bird",
    "C": "worm",
}

map_their_choice_and_my_choice_to_result = {
    "cat": {
        "cat": "ignored",
        "bird": "eaten",
        "worm": "eater",
    },
    "bird": {
        "cat": "eater",
        "bird": "ignored",
        "worm": "eaten",
    },
    "worm": {
        "cat": "eaten",
        "bird": "eater",
        "worm": "ignored",
    },
}

map_result_to_score = {
    "eaten": 0,
    "ignored": 3,
    "eater": 6,
}

def parse_input(message: str) -> List[Tuple[str, str]]:
    # PROMPT: parse into array of lines and then split each by space
    # ------------------
    # (the rest is auto-generated)
    return [line.split(" ") for line in message.splitlines()]

def compute_answer(inputs: List[Tuple[str, str]]) -> int:

    total_score = 0
    for input in inputs:
        their_input = input[0]
        my_input = input[1]
        
        # PROMPT: map my input to choice
        my_choice = map_my_input_to_choice[my_input]
        # PROMPT: map my choice to score
        my_score = map_my_choice_to_score[my_choice]
        # PROMPT: add my score to total score
        total_score += my_score
        # PROMPT: map their input to choice
        their_choice = map_their_input_to_choice[their_input]
        # PROMPT: map their choice and my choice to result
        result = map_their_choice_and_my_choice_to_result[their_choice][my_choice]
        # PROMPT: map result to score
        result_score = map_result_to_score[result]
        # PROMPT: add result score to total score
        total_score += result_score

    return total_score

        
        




