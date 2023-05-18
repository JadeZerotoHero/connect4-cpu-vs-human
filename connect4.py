#FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)

import random

#Copy and paste task 1
valid_inputs = ["1","2","3","4","5","6","7"] #Create a list for valid_inputs

def validate_input(prompt, valid_inputs): # Function validate_input with 2 arguements 'prompt' and 'valid_inputs'.
    while True: #while True loop - combination of for and while loop
        user_input = input(prompt) #user input a value after reading the prompt such as "Please select an option (a, b, c): "
        if user_input in valid_inputs: #if user inputs a value that is in list of valid_inputs
            return user_input
        else: #if user inputs a value that is not in list of valid_inputs, prints "Invalid input, please try again."
            print("Invalid input, please try again.")

#Copy and paste task 2
def create_board():
	row_count = 6
	column_count = 7
	board = [] # Create an empty list assigned to variable 'board'.

	for i in range(0, row_count): # Iterates for 6 rows
		board.append([0] * column_count) # Adds 7 '0's to the existing empty list in 'board' for each of the 6 rows.
	
	return board # Returns a nested list with a list of 7 '0's in a list of 6 rows.

#Copy and paste task 3
def print_board(board):
    #labels the columns from 1-6, as well as the rows using the symbol "|".
    rows = ['1','2','3','4','5','6']
    top = '  1   2   3   4   5   6   7'
    row = [[n] for n in range(0,7)]
    row[0][0] = '|'
    row[1][0] = '|'
    row[2][0] = '|'
    row[3][0] = '|'
    row[4][0] = '|'
    row[5][0] = '|'
    
    #prints out the header of the board.
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O")
    print('')
    print(top)
    
    #prints out the edges of each cell, e.g. "___".
    print(' ' + '--- '*len(rows) + '---' )
    #the logic used to populate each cell of the board, by replacing 0 with a " ", player 1's token with "X" and player 2's token with "O".
    for j in range(0,len(rows)):
        for i in range(1,8):
            if str(board[j][i-1]) == '0':
                cellval = str(board[j][i-1]).replace('0',' ')
            elif str(board[j][i-1]) == '1':
                cellval = str(board[j][i-1]).replace('1','X')
            else:
                cellval = str(board[j][i-1]).replace('2','O')    
            row[j][0] = row[j][0] + ' ' + cellval + ' |'
        print(row[j][0])
        #prints out the edges of each cell, e.g. "___". 
        print(' ' + '--- '*len(rows) + '---' )
    #prints out the bottom of the board.
    print("=============================")
  
#Copy and paste task 4
def drop_piece(board, player, column):
    # Determine the number of rows in the board.
    rows_number = len(board)

    # Iterate through the rows in reverse order (from bottom to top).
    for i in range(rows_number):
        # Check the current cell in the specified column.
        x = board[rows_number - i - 1][column - 1]

        # If the current cell is empty (value is 0):
        if x == 0:
            # Assign the player number (1 or 2) to the cell.
            board[rows_number - i - 1][column - 1] = player
            return True  # Return True, indicating that the piece was successfully dropped.

    # If the function reaches this point, the column is full.
    print("That column is full, please try again.")
    return False  # Return False, indicating that the piece could not be dropped.

def execute_player_turn(player, board):  # Task 5
    # Continue looping until a valid move is made.
    while True:
        # Prompt the player for input, asking for the column to drop the piece into.
        # validate_input ensures that the entered column is within the valid range.
        column_input = validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ", valid_inputs)
        
        # Convert the input string to an integer.
        column = int(column_input)

        # Try to drop the piece into the specified column.
        # If the drop_piece function returns True (i.e., the move is valid), exit the loop and return the column.
        if drop_piece(board, player, column):
            return column

#Copy and paste task 6
def end_of_game(board):
    #Variables for the different game outcomes.
    game_n_over = 0  # Game is not over yet.
    player_1 = 1    # Player 1 has won.
    player_2 = 2    # Player 2 has won.
    draw = 3        # Game has ended in a draw.
    
    # Check for horizontal wins.
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            # Check if there are four non-zero values in a row.
            if board[row][col] != 0 and \
               board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                # Return the winning player.
                if board[row][col] == player_1:
                    return player_1
                else:
                    return player_2
                    
    # Check for vertical wins.
    for row in range(len(board) - 3):
        for col in range(len(board[0])):
            # Check if there are four non-zero values in a column.
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                # Return the winning player.
                if board[row][col] == player_1:
                    return player_1
                else:
                    return player_2
                    
    # Check for diagonal wins (top-left to bottom-right).
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            # Check if there are four non-zero values in a diagonal.
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                # Return the winning player.
                if board[row][col] == player_1:
                    return player_1
                else:
                    return player_2
                    
    # Check for diagonal wins (bottom-left to top-right).
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            # Check if there are four non-zero values in a diagonal.
            if board[row][col] != 0 and \
               board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                # Return the winning player.
                if board[row][col] == player_1:
                    return player_1
                else:
                    return player_2 
                    
    # If there are no empty spaces left on the board, the game is a draw.
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return game_n_over
                
    # If none of the above conditions are met, the game is a draw.
    return draw

#Copy and paste task 7
def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    board = create_board()  # Creates an empty 6x7 game board
    player = 1  # Initializes the current player to be Player 1
    previous_move = -1 #No previous move
    previous_player = -1 #No previous player

    #Main game loop
    while True:
        clear_screen()  # Clears the terminal screen
        print_board(board)  # Prints the current game board

        if previous_move != -1: #Check if there is a previous move and print information about it
            print(f"Player {previous_player} dropped a piece into column {previous_move}")

        # Executes the current player's turn and returns the column number of the move
        col = execute_player_turn(player, board)
        # Checks if the game has ended (either a win or a draw) after the current move
        game_result = end_of_game(board)
        previous_move = col  # Stores the current move as the previous move for the next iteration
        previous_player = player  # Stores the current player as the previous player for the next iteration
        player = 3 - player  # Switches between Player 1 and Player 2 (3 - 1 equal 2, 3 - 2 equals 1. 2 = player 2, 1 = player 1)

        # If the game has ended, print the final game board and the result
        if game_result != 0:
            clear_screen()
            print_board(board)
            if game_result == 1:
                print("Player 1 wins!")
            elif game_result == 2:
                print("Player 2 wins!")
            else:
                print("It's a draw!")
            break

    return None

#Task 8
def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	return None
    
def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")

def main():
    # This is the main loop that runs until the user chooses to exit the game.
    while True:
        clear_screen()  # Clear the console screen for a fresh menu display.

        # Print the main menu with options for the user.
        print("=============== Main Menu ===============")
        print("Welcome to Connect 4!")
        print("1. View rules")
        print("2. Play a local 2 player game")
        print("3. Play a game against the computer")
        print("4. Exit")
        print("=========================================")

        # Prompt the user to choose an option and validate their input.
        game_choice = validate_input("Please choose an option (1-4): ", ["1", "2", "3", "4"])

        # If the user chooses option 1 (View rules):
        if game_choice == "1":
            clear_screen()  # Clear the console screen.
            print_rules()   # Display the rules of the game.
            # Wait for the user to press Enter before returning to the main menu.
            input("Press Enter to return to the main menu.")
            clear_screen()
            
        # If the user chooses option 2 (Play a local 2 player game):
        elif game_choice == "2":
            clear_screen()           # Clear the console screen.
            local_2_player_game()    # Start the local 2 player game.
            # Wait for the user to press Enter before returning to the main menu.
            input("Press Enter to return to the main menu.")
            
        # If the user chooses option 3 (Play a game against the computer):
        elif game_choice == "3":
            clear_screen()
            game_against_cpu()
            
        # If the user chooses option 4 (Exit):
        elif game_choice == "4":
            print("Thanks for playing! Goodbye!")  # Print a farewell message.
            break  # Break out of the while loop to exit the game.

    return None

#Task 9
def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function 
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    while True:
        column = random.randint(1, 7)
        if drop_piece(board, player, column):
            return column

#Task 10
def cpu_player_medium(board, player):
    """
	Executes a move for the CPU on medium difficulty.
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
    for target_player in [player, 3 - player]:
        for col in range(1, 8):
            test_board = [row.copy() for row in board]
            if drop_piece(test_board, target_player, col):
                if end_of_game(test_board) == target_player:
                    drop_piece(board, player, col)
                    return col

    # If neither winning move nor blocking move is available, play a random move
    while True:
        random_col = random.randint(1, 7)
        if drop_piece(board, player, random_col):
            return random_col

#Task 11

def cpu_player_hard(board, player):
    """
    Calculates the best move for the CPU player using the minimax algorithm for board evaluation.
    This function first scores the current board state then performs a search 
    using the minimax algorithm to find the best move for the CPU player.
    Performs the minimax algorithm with basic heuristics.
    It then targets the middle of the board for higher chance of winning rather
    going for the corner empty columns

    Psuedocode:
        function cpu_player_hard:
    define minimax function:
        if depth is 0 || game has ended:
            return score_board
        if maximizing_player:
            find best move for player with highest score
        else:
            find best move for opponent with lowest score   
    initialize best_score and best_col
    set depth limit for search
    prioritize middle column  
    for each column in board:
        create test_board copy
        if dropping piece in column is valid:
            calculate score using minimax algorithm
            update best_score and best_col if necessary
    drop piece in best column found
    return best_col
    """


    # The minimax function returns the best score for a given board state and player.
    def minimax(board, depth, maximizing_player, player):
        # If depth is 0 or the game has ended, return the score of the board.
        if depth == 0 or end_of_game(board) != 0:
            return score_board(board, player)

        if maximizing_player:
            max_score = float('-inf')
            # Iterate through all columns to find the best score.
            for col in range(1, 8):
                test_board = [row.copy() for row in board]
                if drop_piece(test_board, player, col):
                    # Recursively call minimax for the next depth and opposite player.
                    score = minimax(test_board, depth - 1, False, player)
                    max_score = max(max_score, score)
            return max_score

        else:
            min_score = float('inf')
            # Iterate through all columns to find the best score.
            for col in range(1, 8):
                test_board = [row.copy() for row in board]
                if drop_piece(test_board, 3 - player, col):
                    # Recursively call minimax for the next depth and opposite player.
                    score = minimax(test_board, depth - 1, True, player)
                    min_score = min(min_score, score)
            return min_score

    # The score_board function returns the score of the board for the given player.
    def score_board(board, player):
        score = 0

        # Check for wins and assign a high score.
        if end_of_game(board) == player:
            score = 1000
        elif end_of_game(board) == (3 - player):
            score = -1000

        return score

    best_score = float('-inf')
    best_col = None
    depth = 5 # Increase the search depth for better performance

    # Check if middle column is available and prioritize it.
    if drop_piece([row.copy() for row in board], player, 4):
        best_col = 4
    else:
        # Iterate through all columns and find the one with the highest minimax score.
        for col in range(1, 8):
            test_board = [row.copy() for row in board]
            if drop_piece(test_board, player, col):
                score = minimax(test_board, depth - 1, False, player)
                if score > best_score:
                    best_score = score
                    best_col = col

    # Drop the piece in the best column found.
    drop_piece(board, player, best_col)
    return best_col

#Task 12
def game_against_cpu():
    """
    Runs a game of Connect 4 against the computer.

    :return: None
    """
    # Prompt the user to choose a difficulty level
    difficulty = validate_input("Please choose a difficulty level (easy, medium, hard): ", ["easy", "medium", "hard"])

    board = create_board()
    player = 1
    previous_move = -1
    previous_player = -1

    while True:
        clear_screen()
        print_board(board)

        if previous_move != -1:
            print(f"Player {previous_player} dropped a piece into column {previous_move}")

        if player == 1:
            col = execute_player_turn(player, board)
        else:
            if difficulty == "easy":
                col = cpu_player_easy(board, player)
            elif difficulty == "medium":
                col = cpu_player_medium(board, player)
            else:
                col = cpu_player_hard(board, player)
        
        game_result = end_of_game(board)
        previous_move = col
        previous_player = player
        player = 3 - player

        if game_result != 0:
            clear_screen()
            print_board(board)
            if game_result == 1:
                print("Player 1 wins!")
            elif game_result == 2:
                print("Player 2 wins!")
            else:
                print("It's a draw!")
            break
        
if __name__ == "__main__":
    main()
