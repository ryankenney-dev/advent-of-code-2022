from typing import List, Tuple

map_my_input_to_goal = {
    "X": "eaten",
    "Y": "ignored",
    "Z": "eater",
}

map_my_choice_to_score = {
    "worm": 1,
    "bird": 2,
    "cat": 3,
}

map_their_input_to_choice = {
    "A": "worm",
    "B": "bird",
    "C": "cat",
}

map_their_choice_and_my_goal_to_my_choice = {
    "cat": {
        "ignored": "cat",
        "eaten": "bird",
        "eater": "worm",
    },
    "bird": {
        "ignored": "bird",
        "eaten": "worm",
        "eater": "cat",
    },
    "worm": {
        "ignored": "worm",
        "eaten": "cat",
        "eater": "bird",
    },
}

map_result_to_score = {
    "eaten": 0,
    "ignored": 3,
    "eater": 6,
}

def parse_input(message: str) -> List[Tuple[str, str]]:
    # PROMPT: parse into array of lines and then split each by space
    return [line.split(" ") for line in message.splitlines()]

def compute_answer(inputs: List[Tuple[str, str]]) -> int:

    total_score = 0
    for input in inputs:
        their_input = input[0]
        my_input = input[1]

        # PROMPT: map their input to choice
        their_choice = map_their_input_to_choice[their_input]
        # PROMPT: map my input to goal
        my_goal = map_my_input_to_goal[my_input]
        # PROMPT: map their choice and my goal to my choice
        my_choice = map_their_choice_and_my_goal_to_my_choice[their_choice][my_goal]
        # PROMPT: map my choice to score
        my_score = map_my_choice_to_score[my_choice]
        # PROMPT: add my score to total score
        total_score += my_score

        result = my_goal 

        # PROMPT: map result to score
        result_score = map_result_to_score[result]
        # PROMPT: add result score to total score
        total_score += result_score

    return total_score

        
        




