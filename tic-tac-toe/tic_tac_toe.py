import random

def draw_board(board):
    """This function prints out the board that it was passed."""
    print('')
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]}")


def get_player_and_computer_letters():
    """
    Lets the player type which letter they want to be.

    Returns a list with the player's letter as the first item and the computer's
    letter as the second item.
    """
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


# This function must be completed
def play_again():
    """
    Determines if the player wants to play again.

    It should as the player if they want to play again, then read input from the
    player to determine if they typed some value that begins with the letter
    "y". If the value does begin with "y", then return True. Otherwise, return
    False.
    """
    print('If you want to play again type "y" and press enter')
    return input().lower() == 'y'


def make_move(board, letter, move):
    """Set the board at index move to the provided letter"""
    board[move] = letter


# This function must be completed
def is_winner(board, letter):
    """
    Determines if the specified letter is a winner.

    Given the board and the player's letter, this function returns True if that
    player has won.
    """
    pass


def is_space_free(board, move):
    """Return True if the value in board at move is " "."""
    return board[move] == " "


# This function must be completed
def get_player_move(board):
    """
    Prompt the player for their move and return their value as an integer.

    This function insures that the board space in which the player wants to play
    is empty. If the player indicates a square that already has a value in it,
    then the function tells the player that is an invalid move and prompts the
    player, again, for a value.
    """
    while True:
        print('Place your mark.')
        move = input()
        if move not in "012345678":
            print('Invalid move. Try again.')
            continue
        else:
            move = int(move)

        if move in range(9) and is_space_free(board, move):
            return move

        print('Invalid move. Try again.')


# This function must be completed
def get_random_move(board):
    """
    Returns a valid random move for the computer from an empty space in the
    board.

    To get nice random moves, consider using the random.shuffle method, here.
    """
    free_spaces = set()
    for idx in range(len(board)):
        if is_space_free(board, idx):
            free_spaces.add(idx)
    return random.randint(0, len(free_spaces)-1)


# This function must be completed
def is_board_full(board):
    """
    Return True if every space on the board has been taken. Otherwise return
    False.
    """
    for idx in range(len(board)):
        if is_space_free(board, idx):
            return False
    return True

print("Welcome to Tic Tac Toe!")

while True:
    board = [" "] * 10
    player, computer = get_player_and_computer_letters()
    if player == "X":
        turn = "player"
    else:
        turn = "computer"
    game_in_progress = True

    while game_in_progress:
        if turn == "player":
            draw_board(board)
            move = get_player_move(board)
            make_move(board, player, move)

            if is_winner(board, player):
                draw_board(board)
                print("Hooray! You have won the game!")
                game_in_progress = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        else:
            move = get_random_move(board)
            make_move(board, computer, move)

            if is_winner(board, computer):
                draw_board(board)
                print("The computer has beaten you! You lose.")
                game_in_progress = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"
    if not play_again():
        break
