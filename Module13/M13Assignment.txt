# UPDATE: AI Programming 
# Hunter Brown
# 09/30/2023

"""In this assignment, you will use an AI system to write a Python program for you, then evaluate the results!
Purpose
For future programming classes, the goal is for you to really learn programming. So I expect you to figure out your own solution, instead of just using AI or other tools that give you a solution.  And make sure you really understand any code that you submit - don’t submit code that doesn’t make sense to you.
But for this assignment, I want you to experiment with AI, and see what kind of Python code it gives you and whether you can understand that code.

Instructions
Step 1
I am going to give you an algorithm. Can you identify what it represents?

If your opponent has two in a row play the remaining square
Otherwise, if there’s a move that creates two lines of two in a row, play that
Otherwise, if the center square is free play there
Otherwise if your opponent has played in a corner play in the opposite corer
Otherwise if there’s an empty corner play there
Otherwise play on any empty square

Step 2
Use an AI ‘assistant’ to implement the algorithm above into code.

After you've picked an AI tool use the tool as follows:
Ask the AI assistant what the algorithm is for. Did it get the answer correct? Did it offer any improvements
Ask the AI tool to write a Python program for you based on the algorithm above.
Copy and paste the Python code from the AI into Replit, or the IDE of your choice, and test it out: does it work correctly in all cases?  Make sure to test the edge cases such as invalid inputs.  How could you have changed your original instructions to get better results?
Do you understand all the code that was produced? ChatGPT often writes code with functions (“def” statements, which is the topic of our next module), and also with “try” and “except”, which are used for handling errors (called “exceptions”). That is covered next semester in CS 110B, 111B, and 131B.  Which parts don’t you understand?
Do you have any ideas for how to improve the code, or to change it so that you understand it better?  Please make at least one change, and run the modified program to make sure it works."""

# ChatGPT4:

# Step 1: What does the algorithm represent?

""""The algorithm you've described is most likely for a game of Tic Tac Toe. It’s giving strategies on how to play effectively based on the opponent's moves and the current state of the game board.

Here’s a breakdown of the rules mentioned in the algorithm:

Play the remaining square when the opponent has two in a row.

This is a defensive move to block the opponent from winning by having three in a row.
If there’s a move that creates two lines of two in a row, play that.

This is an aggressive move, focusing on creating multiple winning opportunities.
If the center square is free, play there.

This is a strategic move, as controlling the center can be advantageous, giving more opportunities to create three in a row.
If your opponent has played in a corner, play in the opposite corner.

This is a defensive and strategic move to block potential winning situations for the opponent.
If there’s an empty corner, play there.

Occupying a corner can be strategically important as it can potentially be part of two winning lines (diagonal and the respective row or column).
Otherwise, play on any empty square.

This is the fallback strategy when there are no strategically significant moves available, simply occupy any available space.
This algorithm represents a combination of defensive and offensive strategies, aiming to prevent the opponent from winning while maximizing the player's own chances of winning. It’s a set of heuristics that are simple yet quite effective for a game like Tic Tac Toe."""

# Step 2:  Ask to implement the algorithm above into Python code.
# USER: implement this into python code
# GPT-4 Response:
# "You can implement this algorithm in Python using a 2D list to represent the Tic Tac Toe board, where each cell can be 'X', 'O', or an empty string representing an empty cell. Here is a simple implementation:"
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-'*5)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.switch_player()
        else:
            print("Invalid Move. Try again.")

    def is_winner(self, player):
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def play_best_move(self):
        opponent = 'O' if self.current_player == 'X' else 'X'
        
        # Check if there is a winning move or a block needed
        for row, col in self.get_available_moves():
            self.board[row][col] = self.current_player
            if self.is_winner(self.current_player):
                return
            self.board[row][col] = ' '

        # Check if the opponent has two in a row and play the remaining square.
        for row, col in self.get_available_moves():
            self.board[row][col] = opponent
            if self.is_winner(opponent):
                self.board[row][col] = self.current_player
                self.switch_player()
                return
            self.board[row][col] = ' '
        
        # If the center square is free, play there.
        if self.board[1][1] == ' ':
            self.play(1, 1)
            return
        
        # If the opponent has played in a corner, play in the opposite corner.
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for row, col in corners:
            if self.board[row][col] == opponent:
                opposite_row, opposite_col = 2 - row, 2 - col
                if self.board[opposite_row][opposite_col] == ' ':
                    self.play(opposite_row, opposite_col)
                    return
        
        # If there’s an empty corner, play there.
        for row, col in corners:
            if self.board[row][col] == ' ':
                self.play(row, col)
                return
        
        # Otherwise, play on any empty square.
        row, col = self.get_available_moves()[0]
        self.play(row, col)


if __name__ == "__main__":
    game = TicTacToe()
    while not game.is_board_full() and not any(game.is_winner(player) for player in ['X', 'O']):
        game.print_board()
        # THIS IS WHERE I CHANGED THE ORIGINAL CODE
        if game.current_player == 'X':
            while True:
                try:
                    print("Enter -1 to quit at any time.")
                    row = int(input("Enter the row (0-2): "))
                    col = int(input("Enter the column (0-2): "))

                    if row == -1 or col == -1:
                        print("Thanks for playing!")
                        exit()
            
                    if 0 <= row <= 2 and 0 <= col <= 2 and game.board[row][col] == ' ':
                        game.play(row, col)
                        break
                    else:
                        print("Invalid input, please enter numbers between 0 and 2")    

                except ValueError:
                    print("Invalid input, please enter a valid number between 0 and 2")
        else:
            game.play_best_move()
        
        if game.is_winner('X'):
            game.print_board()
            print("Player X wins!")
        elif game.is_winner('O'):
            game.print_board()
            print("Player O wins!")
        elif game.is_board_full():
            game.print_board()
            print("It's a draw!")

# "This Python program initializes a Tic Tac Toe game and allows a human player to play as 'X' and the computer to play as 'O', making its moves based on the given algorithm."

# SAMPLE OUTPUT
# ----------------------
"""$ python3 M13Assignment.py 
 | | 
-----
 | |
-----
 | |
-----
Enter the row (0-2): 0
Enter the column (0-2): 2
 | |X
-----
 | |
-----
 | |
-----
 | |X
-----
 |O|
-----
 | |
-----
Enter the row (0-2): 2
Enter the column (0-2): 2
 | |X
-----
 |O|
-----
 | |X
-----
 | |X
-----
 |O|O
-----
 | |X
-----
Enter the row (0-2): 1
Enter the column (0-2): 0
 | |X
-----
X|O|O
-----
 | |X
-----
 | |X
-----
X|O|O
-----
O| |X
-----
Enter the row (0-2): 0
Enter the column (0-2): 2
Invalid Move. Try again.
 | |X
-----
X|O|O
-----
O| |X
-----
Enter the row (0-2): 0
Enter the column (0-2): 1
 |X|X
-----
X|O|O
-----
O| |X
-----
O|X|X
-----
X|O|O
-----
O| |X
-----
Enter the row (0-2): 2
Enter the column (0-2): 2
Invalid Move. Try again.
O|X|X
-----
X|O|O
-----
O| |X
-----
Enter the row (0-2): 2
Enter the column (0-2): 1
O|X|X
-----
X|O|O
-----
O|X|X
-----
It's a draw!"""

# Shortcomings:
"""Enter the row (0-2): 56
Enter the column (0-2): 56
Traceback (most recent call last):
  File "M13Assignment.py", line 151, in <module>
    game.play(row, col)
  File "M13Assignment.py", line 76, in play
    if self.board[row][col] == ' ':
IndexError: list index out of range
-----------------------------------
Enter the row (0-2): a
Traceback (most recent call last):
  File "M13Assignment.py", line 149, in <module>
    row = int(input("Enter the row (0-2): "))
ValueError: invalid literal for int() with base 10: 'a'
-----------------------------------
Enter the row (0-2): -77
Enter the column (0-2): -2
Traceback (most recent call last):
  File "M13Assignment.py", line 152, in <module>
    game.play(row, col)
  File "M13Assignment.py", line 77, in play
    if self.board[row][col] == ' ':
IndexError: list index out of range
-----------------------------------
Enter the row (0-2):
Traceback (most recent call last):
  File "M13Assignment.py", line 150, in <module>
    row = int(input("Enter the row (0-2): "))
ValueError: invalid literal for int() with base 10: ''
"""

# The main edge case issues are if the user enters a value out of the 0 to 2 range or a non-integer value. I would add some functions to handle these cases and print a message to the user to enter a valid value. Nothing entered also causes the program to crash, so I would add a check for that as well.
# The instructions I could have given were for the program to make sure the user gives valid input and to handle any errors that may occur. I could have also asked the program to print a message to the user if they enter an invalid value and for the program to continue running.

# I understand a lot of the code here, due to experience with JavaScript functions and the *similar* readablity to Python functions. I also understand the logic behind the code, but I don't understand the syntax for the "all" function and the "get_available_moves" function. I would need to do some research to understand these functions better. Another thing that confuses me is the __init__ function because of the way its named and I am not sure why it needs to be named with the "__" before and after the name. I would need to do some research to understand this better as well.

# I would add checks for user input "

"""
ORIGINAL OUTPUT FROM GPT-4:
if game.current_player == 'X':
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))
    game.play(row, col)

CHANGES TO THE CODE TO IMPORVE USER EXPERIENCE:
if game.current_player == 'X':
    while True:
        try:
            print("Enter -1 to quit at any time.")
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if row == -1 or col == -1:
                print("Thanks for playing!")
                exit()
            
            if 0 <= row <= 2 and 0 <= col <= 2 and game.board[row][col] == ' ':
                game.play(row, col)
                break
            else:
                print("Invalid input, please enter numbers between 0 and 2")
                
        except ValueError:
            print("Invalid input, please enter a valid number between 0 and 2")

SAMPLE OUTPUT WITH NEW CODE:
------------------------------
Enter -1 to quit at any time.
Enter the row (0-2): 26
Enter the column (0-2): 24
Invalid input, please enter numbers between 0 and 2
Enter -1 to quit at any time.
Enter the row (0-2): -17
Enter the column (0-2): hunter
Invalid input, please enter a valid number between 0 and 2
Enter -1 to quit at any time.
Enter the row (0-2): -1
Enter the column (0-2): -1
Thanks for playing!
"""



