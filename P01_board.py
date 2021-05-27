######################################################################
# Author: Anish Kharel
# Username: Kharel
#
# Assignment: P01: To demonstrate knowledge of classes, functions, and event handling
#
# Purpose: Simulates nims game virtually to demonstrate classes, class collabaration, and GUI & Event handling
###################################################################
from P01_nimsClass import *
from tkinter import *


class GUI:


    def __init__(self,root,balls):
        """
        Constructor function for the GUI class

        :param root: A TK object where the main game board will be played on
        :param balls: The amount of starting balls to fill the inital board
        """
        self.root = root
        self.balls = balls
        pass

    def draw_board(self):
        """
        This function's purpose is to make the intitial gui with initial balls to be further updated by other methods
        """
        message = ""
        heading = Label(self.root, text="Virtual Nims", font=("sans", 50)).grid(row=1, column=1, columnspan=4,padx= 50)
        labelnims = Label(self.root, text="Balls remaining:",font=("sans", 20)).grid(row=2, column=1, columnspan=2)
        labelask=Label(self.root, text="Please enter how many balls\n you would like to remove:", font=("sans", 15)).grid(row=2, column=3, columnspan=2,padx=40)



        self.update_console()                   # call to get the default console in board
        self.update_board(self.balls)           # call to get the default canvas with initial balls
        self.get_input()                        # call to get the buttons in the board

        self.root.update()



    def get_input(self, balls = -1):
        """
        This function's purpose is to handle the event of button clicks for the player input

        :param balls: The amount of balls in the middle
        :return: the balls in the middle - the balls removed by player
        """
        def buttonCLick(number):
            """
            This functions purpose is to trigger and subtract the user move from the amount in the middle

            :param number: the button that was clicked and it corresponding number
            :return: balls_left in the middle
            """
            self.balls_left = number
            self.root.quit()
            return self.balls_left

        font = 40
        button1 = Button(self.root, text="1", width=4, font=("sans", font), command=lambda: buttonCLick(1)).grid(
            row=3, column=3)
        button2 = Button(self.root, text="2", width=4, font=("sans", font), command=lambda: buttonCLick(2)).grid(
            row=3, column=4)
        button3 = Button(self.root, text="3", width=4, font=("sans", font), command=lambda: buttonCLick(3)).grid(
            row=4, column=3)
        button4 = Button(self.root, text="4", width=4, font=("sans", font), command=lambda: buttonCLick(4)).grid(
            row=4, column=4)

        if str(balls) == -1:
            self.root.update()
        else:
            self.root.mainloop()
        return self.balls_left

    def update_board(self, balls):
        """
        This function's purpose is to update the canvas widget which displays the amount of balls in the middle after
        every turn.

        :param balls: The amount of balls actively in the middle
        """
        table = Canvas(self.root, width=300, height=300, bg="white")
        table.grid(row=3, column=1, columnspan=2, rowspan=3, padx=25, pady=25)
        table.create_oval(15, 300, 300, 15)
        table.create_text(155, 155, text=balls, font=("sans", 100))

        self.root.update()

    def update_console(self, balls=0, move_maker=""):
        """This function's purpose is to update the console to display the most recent move, whether by the computer
        or by player and by how much

        :param balls: Amount of balls removed in that turn
        :param move_maker: Whose turn it was
        """
        box = Entry(self.root, width=42, font=("sans", 12))
        box.grid(row=5, column=3, columnspan=2, padx=15)
        box.delete(0)
        if len(move_maker) == 0:
            box.insert(0, "There are currently no moves to be shown1")
        else:
            box.insert(0, move_maker + " has removed the following amount of balls: "+str(balls))

        self.root.update

    def error_message(self, message):
        """This function's purpose is to display error message using GUIs

        :param message: The message you want the GUI window to display
        """

        root = Tk()
        l = Label(root, text=message, width=50).grid(row=1, column=1)
        root.mainloop()

    def winner_message(self, turn):
        """
        This Function's purpose it to display the winner message using GUIs

        :param turn: Who won (console or player)
        """
        if turn == "Player":
            color = "lightgreen"
        else:
            color = "red"
        self.root.destroy()
        winmes = Tk()
        winmes.config(bg=color)
        winmes.geometry("700x175")

        winner_message = Label(winmes, text=str(turn)+" has won the Game.",font=("sans",35),bg = color).grid(row=1, column=1, pady=25, padx=50)
        replay_message = Label(winmes, text="Please press the green play button to replay", font=("sans", 15), bg=color).grid(row=2,column=1)

        winmes.after(5000, lambda: winmes.destroy())  # Destroy the widget after 30 seconds
        winmes.mainloop()




