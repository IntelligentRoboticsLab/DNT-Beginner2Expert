import random

possible_actions = ["rock", "paper", "scissors"]


def get_user_input(question):
    """ Wrapper function for input, needed for testing. """
    return input(question)


def get_user_action(get_user_input):
    """
    Ask the user for input, either rock, paper or scissors. If the input string
    is not rock, paper or scissors it should ask again. Return the resulting
    input.
    """
    action = ""

    while (action not in possible_actions):
        action = get_user_input(f"Enter a choice {possible_actions}: ")

    return action


def get_computer_move():
    """ Returns a random possible action. """
    return random.choice(possible_actions)


def print_result(user_action, computer_action):
    """ Prints the results. """
    print(f"You played {user_action}, the computer played {computer_action}.")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


def play(get_user_input):
    """ Play one game of rock paper scissors. """
    user_action = get_user_action(get_user_input)
    computer_action = get_computer_move()

    print_result(user_action, computer_action)


def wants_to_play_again(get_user_input):
    """
    Asks the user if they want to play again. If they do, returns True else
    returns False.
    """
    choice = ""

    while (choice not in ["yes", "no"]):
        choice = get_user_input("Do you want to play again? ")

    return choice == "yes"


def run(get_user_input):
    """ Entry point to the program. You can write your code below. """
    while True:
        play(get_user_input)

        if not wants_to_play_again(get_user_input):
            break


if __name__ == "__main__":
    run(get_user_input)
