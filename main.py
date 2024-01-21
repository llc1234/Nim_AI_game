import random


q_values = {}


def display_pins(pins):
    for _ in range(pins):
        print(" | ", end="")
    print("")


def player_turn(pins):
    while True:
        try:
            move = int(input("Enter pins to remove (1-3): "))
            if 1 <= move <= 3 and move <= pins:
                return move
            else:
                print("Invalid move")
        except ValueError:
            print("Invalid input")


def ai_turn(pins):
    global q_values

    max_move = min(3, pins)

    if random.random() < 0.8 and (pins, max_move) in q_values:
        move = q_values[(pins, max_move)]
    else:
        move = random.randint(1, max_move)

    print("AI removes", move)
    return move


def update_q_values(prev_pins, move, current_pins, reward):
    global q_values

    alpha = 0.1
    gamma = 0.9

    current_q_value = q_values.get((prev_pins, move), 0)

    available_actions = [a for a in range(1, min(4, current_pins + 1))]
    if available_actions:
        max_future_q = max(q_values.get((current_pins, a), 0) for a in available_actions)
    else:
        max_future_q = 0

    updated_q_value = current_q_value + alpha * (reward + gamma * max_future_q - current_q_value)
    q_values[(prev_pins, move)] = updated_q_value


def nim_game():
    global q_values
    pins = 10
    player_turns = True

    while pins > 0:
        display_pins(pins)

        if player_turns:
            move = player_turn(pins)
        else:
            move = ai_turn(pins)

        move = max(1, move)

        prev_pins = pins
        pins -= move
        player_turns = not player_turns

        if not player_turns:
            update_q_values(prev_pins, move, pins, reward=1 if pins == 0 else 0)

    display_pins(pins)
    if player_turns:
        print("-------------------------------------------------- Congratulations. You win!")
    else:
        print("-------------------------------------------------- AI wins")

    print(q_values)


if __name__ == "__main__":
    print("Nim Game!")
    while True:
        q_values = {}
        nim_game()
        print("New Game!")


"""

import random


def display_pins(pins):
    print("Current pins:", pins)
    print(" " * 15 + "| " * pins)


def player_turn(pins):
    while True:
        try:
            move = int(input("Your turn. Enter pins to remove (1-3): "))
            if 1 <= move <= 3 and move <= pins:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def ai_turn(pins):
    max_move = min(3, pins)
    move = random.randint(1, max_move)
    print("AI removes", move, "pins.")
    return move


def nim_game():
    pins = 10
    player_turns = True

    while pins > 0:
        display_pins(pins)

        if player_turns:
            move = player_turn(pins)
        else:
            move = ai_turn(pins)

        pins -= move
        player_turns = not player_turns

    display_pins(pins)
    if player_turns:
        print("Congratulations! You win!")
    else:
        print("AI wins. Better luck next time.")


if __name__ == "__main__":
    print("Welcome to Nim Game!")
    while True:
        nim_game()

"""


"""

import random


last_move = 0
last_row = 0

available_moves = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]


def display_pins(pins):
    # print("Current pins:", pins)
    # print(" " * 15 + "| " * pins)

    for _ in range(pins):
        print(" | ", end="")

    print("")


def player_turn(pins):
    while True:
        try:
            move = int(input("Your turn. Enter pins to remove (1-3): "))
            if 1 <= move <= 3 and move <= pins:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def ai_turn(pins, row):
    global last_move, last_row

    #max_move = min(3, pins)
    # move = random.randint(1, max_move)

    move = random.choice(available_moves[row])

    if not len(available_moves[row + move]) == 1:
        last_move = move
        last_row = row

    print("AI removes", move, "pins.")
    return move


def nim_game():
    global available_moves, debug_list

    pins = 10
    player_turns = True
    row = 0

    while pins > 0:
        display_pins(pins)

        if player_turns:
            move = player_turn(pins)
        else:
            move = ai_turn(pins, row)

        pins -= move
        player_turns = not player_turns

        row += 1

    display_pins(pins)
    if player_turns:
        print("Congratulations! You win!")

        if not len(available_moves[last_move]) == 1:
            available_moves[last_row].remove(last_move)

        for i in range(len(available_moves)):
            print(f" {available_moves[i]} ", end="")

    else:
        print("AI wins. Better luck next time.")


if __name__ == "__main__":
    print("Welcome to Nim Game!")
    while True:
        nim_game()
        print("\n\nNew Game!")"""
