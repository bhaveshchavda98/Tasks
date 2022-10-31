'''
In this project you will build a simplified, one-player version of the classic board game Battleship!
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid.
The player will have 10 guesses to try to sink the ship.
To build this game we will use our knowledge of lists, conditionals and functions in Python.
We will go step by step, given solutions at the end you will find the solution(complete code stored
in battleship.py).
'''
board  = []
[board.append('O') for i in range(5)]
print(board)
print(len(board))
