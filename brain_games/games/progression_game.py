import random
from brain_games.games.games_engine import launch_game
from brain_games.games.games_constants import MAX_NUMBER, \
    MAX_PROGRESSION_LENGTH, MIN_PROGRESSION_LENGTH, \
    MAX_PROGRESSION_STEP, MIN_PROGRESSION_STEP


game_rules = 'What number is missing in the progression?'


def makeProgression(length, first, step):
    result = []
    for i in range(length):
        result.append(str(first + i * step))
    return result


def generate_question(progression, index):
    progression_copy = progression[:]
    progression_copy[index] = '..'
    return ' '.join(progression_copy)


def generate_round():
    length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    first_element = random.randint(0, MAX_NUMBER)
    step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    progression = makeProgression(length, first_element, step)
    hidden_element_index = random.randint(0, length - 1)
    question = generate_question(progression, hidden_element_index)
    answer = progression[hidden_element_index]
    return (question, answer)


def run_game():
    launch_game(generate_round, game_rules)