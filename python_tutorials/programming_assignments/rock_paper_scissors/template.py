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
    pass


def get_computer_move():
    """ Returns a random possible action. """
    pass


def print_result(user_action, computer_action):
    """ Prints the results. """
    pass


def play(get_user_input):
    """ Play one game of rock paper scissors. """
    pass


def wants_to_play_again(get_user_input):
    """
    Asks the user if they want to play again. If they do, returns True else
    returns False.
    """
    pass


def run(get_user_input):
    """ Entry point to the program. You can write your code below. """
    pass

if __name__ == "__main__":
    run(get_user_input)
