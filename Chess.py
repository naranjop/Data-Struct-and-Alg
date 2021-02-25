#  File: Chess.py

#  Description: prints the total number of ways in which Queens can be placed
#  in a n by n chess board without being able to capture each other.

#  Date Created: 10/23/2020

#  Date Last Modified: 10/23/2020

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)
  

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col, solutions):
    if (col == self.n):
      if self.board not in solutions:
        return True
      return False
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          if self.recursive_solve(col + 1, solutions):
            return True
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self, solutions):
    if self.recursive_solve(0, solutions):
      solutions.append(self.board)
      return solutions
    else:
      return -1
        
              
def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)
  num = 0
  solutions = []

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  keep_going = True
  while keep_going: 
    solutions = game.solve(solutions)
    if solutions == -1:
      break
    num += 1
    game = Queens(n)

  # print the number of solutions
  print(num)


if __name__ == "__main__":
  main()
