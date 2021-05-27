######################################################################
# Author: Anish Kharel
# Username: Kharel
#
# Assignment: P01: To demonstrate knowledge of classes, functions, and event handling
#
# Purpose: Simulates nims game virtually to demonstrate classes, class collabaration, and GUI & Event handling
###################################################################
import P01_nimsClass as nim
import P01_board as board
import time
from turtle import *
from tkinter import *


def get_starter_balls():
    """
    This functions main purpose is to start the program and retrieve the starter balls and state the rules and how to
    play the game of virtual nims
    """
    root = Tk()
    root.title("Game of Nims")
    board2 = board.GUI(root, 0)
    nims2 = nim.Nims(board2)

    def button_click():
        """
        Handles the submit button click event by quiting the window and checking the inout to make sure it is within
        range using the nims class

        :return: return the balls inputted into entry
        """
        if nims2.balls_checker(balls_entry.get()):
            balls = balls_entry.get()
            root.quit()

            return balls
        else:
           board2.error_message("Invalid input \n Please input a number greater than 15")


    title = Label(root, width=50, text="Welcome to the virtual game of Nims", bd=8).grid(row=1, column=2, columnspan=2,
                                                                                           pady=8)

    directions = Label(root, text="Rules:").grid(row=2, column=2)                     # A label widget to explain rules
    lrules = Label(root,
                   text="two players alternate in removing the ball from the middle \n On each turn, a player can"
                        "remove up to 4 balls provided \nall stones come from the same pileThe player that takes"
                        "\n the last stone/s from the only remaining pile wins the game").grid(row=3, column=2,
                                                                                               pady=3)

    numberask = Label(root, text="Please enter the number you want to start with(greater than 15):").grid(row=2,
                                                                                                          column=3,
                                                                                                          padx=10)

    balls_entry = Entry(root, width=20)                     # A place for the user to input amount of starter balls
    balls_entry.grid(row=3, column=3, pady=5, padx=5)

    submit_button = Button(root, width=25, text="Submit", command=button_click)
    submit_button.grid(row=4, column=2, columnspan=2, pady=10)

    e = Entry(root, width=35)

    root.mainloop()
    global balls_left
    balls_left = button_click()
    root.destroy()




def main():
    global balls_left
    get_starter_balls()                        #Get the starter number of balls

    root = Tk()                                 # instantiate root object as TK
    gui = board.GUI(root, balls_left)           # instantiate gui object as gui
    nims = nim.Nims(gui)                        # instatntiate nims object as nims
    gui.draw_board()                            # draw the initial board to start off the game

    while True:                                 # loop to keep the game going until it breaks off from inside

        player_move = gui.get_input(balls_left)                 # Get players move
        balls_left = int(balls_left) - int(player_move)
        gui.update_console(player_move, "Player")               # Update the console to display the players move
        gui.update_board(balls_left)                            # Update the new amount of balls into the GUI

        if nims.game_end(balls_left):                           # Game end checker
            move = "Player"
            break
        time.sleep(1.5)                                         # timing to give a more of a game and less robotic touch

        comp_move = nims.computer_move(balls_left)              # Computers move
        balls_left = balls_left - comp_move
        gui.update_console(comp_move, "Console")                # Update the console to display the computers move
        gui.update_board(balls_left)                            # Update the board with new amount of balls
        if nims.game_end(balls_left):                           # game end checker
            move = "Console"
            break

    time.sleep(1)                                               # slowed down for smoothness and game effect
    gui.winner_message(move)                                    # Displayes the winner and give direction on how to replay
















main()
