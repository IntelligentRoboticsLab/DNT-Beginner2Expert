import time
import template
import unittest
from unittest import mock
import pytest
import re


possible_actions = ["paper", "rock", "scissors"]
status = re.compile("You played (?:rock|paper|scissors), the computer played (?:rock|paper|scissors).")
all_results = [
    "Both players selected rock. It's a tie!",
    "Both players selected paper. It's a tie!",
    "Both players selected scissors. It's a tie!",
    "Rock smashes scissors! You win!",
    "Paper covers rock! You lose.",
    "Paper covers rock! You win!",
    "Scissors cuts paper! You lose.",
    "Scissors cuts paper! You win!",
    "Rock smashes scissors! You lose."
]


class EndError(Exception):
    """ Defines a custom exception to ensure it's not raised elsewhere. """
    pass


def noop(_):
    """ Defines a function that can be used for mocking. """
    pass


class TestGetUserAction(unittest.TestCase):
    @pytest.mark.timeout(1)
    def test_get_user_action_valid_input(self):
        for action in possible_actions:
            assert template.get_user_action(lambda _: action) == action

    @mock.patch(__name__ + ".noop", side_effect=("test", EndError))
    def test_get_user_action_invalid_input(self, mock_noop):
        with self.assertRaises(
            EndError,
            msg="""When getting user actions, you did not ask for new
                        input after invalid input.""",
        ):
            template.get_user_action(mock_noop)
        self.assertEqual(mock_noop.call_count, 2)


class TestGetComputerMove(unittest.TestCase):
    def test_get_computer_move(self):
        """ Tests if computer returns a valid move. """
        res = {template.get_computer_move() for _ in range(100)}
        assert sorted(list(res)) == possible_actions


class TestPlay(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_play_valid_input(self):
        for action in possible_actions:
            template.play(lambda _: action)
            (out, _) = self.capsys.readouterr()
            out = out.split("\n")
            assert status.match(out[0])
            assert out[1] in all_results


class TestWantsToPlayAgain(unittest.TestCase):
    @pytest.mark.timeout(1)
    def test_wants_to_play_again_valid_input(self):
        assert template.wants_to_play_again(lambda _: "yes") == True
        assert template.wants_to_play_again(lambda _: "no") == False

    @mock.patch(__name__ + ".noop", side_effect=("test", EndError))
    def test_wants_to_play_again_invalid_input(self, mock_noop):
        with self.assertRaises(
            EndError,
            msg="""
                When getting user actions, you did not ask for new input
                after invalid input.
                """,
        ):
            template.get_user_action(mock_noop)
        assert mock_noop.call_count == 2


class TestRun(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    @pytest.mark.timeout(1)
    @mock.patch(__name__ + ".noop", side_effect=("rock", "yes", "paper", "no"))
    def test_wants_to_play_again_invalid_input(self, mock_noop):
        template.run(mock_noop)
        (out, _) = self.capsys.readouterr()
        out = out.split("\n")
        assert status.match(out[0])
        assert out[1] in all_results
        assert status.match(out[2])
        assert out[3] in all_results

