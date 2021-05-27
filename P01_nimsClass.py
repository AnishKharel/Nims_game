######################################################################
# Author: Anish Kharel
# Username: Kharel
#
# Assignment: P01: To demonstrate knowledge of classes, functions, and event handling
#
# Purpose: Simulates nims game virtually to demonstrate classes, class collabaration, and GUI & Event handling
###################################################################
from P01_board import *
import random

class Nims:

    def __init__(self, board):
        """
        Constructor of the Nims class
        :param board: GUI board to collaborate with the class
        """
        self.board = board


    def computer_move(self, balls_left):
        """
        This functions purpose is to play the computer move and holds the algorithm to give the computer the edge
        :param balls_left: The amount of balls left in the middle
        :return: The computers move(The amount the console removed)
        """
        if balls_left % 5 == 0:
            return random.randrange(1, 4)          # if the number is perfectly divisible by 5 then random move
        else:

            return balls_left % 5                   # Computer always gets to numbers divisible by 5

    def game_end(self, balls):
        """
        This functions purpose is to check whether the game is over or not

        :param balls: The amount of balls in the middle
        :return: Whether the game is over or not
        """
        if int(balls) > 0:                      # simple control to check whether there are any balls in the middle
            return False
        else:
            return True

    def balls_checker(self, balls):
        """
        This function insures that the starting balls are more than 15
        :param balls: The user inputted balls
        :return: Whether the balls are more than 15 or not
        """
        if int(balls) > 15:                    # Simple control to insure the input is a minimum of 15
            return True
        return False

