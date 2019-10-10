# ---------------- Global Variables --------------- #

# Game Board
board = ["-", "-", "-",
          "-", "-", "-", 
          "-", "-", "-", ]

# If game is still over
game_still_going = True

# Winner or tie
winner = None

# Current Turn 
current_player = "x"

# Display the board 
def display_board():
  print (board[0] + " | " + board[1] + " | " + board[2])
  print (board[3] + " | " + board[4] + " | " + board[5])
  print (board[6] + " | " + board[7] + " | " + board[8]) 
  print()

# Play game of tic-tac-toe1
def play_game():
  # Display initial board
  display_board()
  # While the game is still going
  while game_still_going:
    # Handle a single turn of player 
    handle_turn(current_player)
    # Check if game has ended 
    check_if_game_over()
    # Flip to the other player 
    flip_player()
  # The game has ended 
  if winner == 'x' or winner == 'o':
    print(winner + " is the winner.")
  elif winner == None:
    print(" It is a tie")


# Handle a single turn of a player 
def handle_turn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  
  valid = False
  while not valid:
    # while entered position is not in the list 
    while position not in ['1','2','3','4','5','6','7','8','9']:
      position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    # prevents overriding values 
    if board[position] == "-":
      valid = True
    else:
      print("Enter another value.")
      print()
  board[position] = player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_for_tie()


def check_for_winner():
  # Set up gloal variables
  global winner
  # check rows
  row_winner = check_rows()
  # check columns
  column_winner = check_columns()
  # check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    # no win
    winner = None
  return 

def check_rows():
  # global variable 
  global game_still_going
  # checks if either/all row have same value 
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any rows have a match, the game stops 
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner (x or o)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  # global variable 
  global game_still_going
  # checks if either/all column have same value 
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  # If any column have a match, the game stops 
  if col_1 or col_2 or col_3:
    game_still_going = False
  # Return the winner (x or o)
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return


def check_diagonals():
  # global variable 
  global game_still_going
  # checks if either/all column have same value 
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  # If any column have a match, the game stops 
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner (x or o)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]
  return


def check_for_tie():
  # Global Variable
  global game_still_going
  if '-' not in board:
    game_still_going = False
  return


def flip_player():
  # Global variable 
  global current_player
  # if the current player was x, then change it to o, else x
  if current_player == 'x':
    current_player = 'o'
  elif current_player == 'o':
    current_player = 'x'
  return 

play_game()