def create_board():
    # Create a 3x3 board filled with spaces
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)
    return board

def print_board(board):
    # Print the current state of the board
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def get_move(player):
    while True:
        try:
            # Prompt the player for their move
            row = int(input(f"Player {player}, enter the row (0-2): "))
            col = int(input(f"Player {player}, enter the column (0-2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

def make_move(board, player, row, col):
    # Place the player's marker on the board if the cell is empty
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("This spot is already taken. Try again.")
        return False

def check_win(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check columns
    for col in range(3): 
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_draw(board):
    # Check for a draw by verifying if all cells are filled
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def tic_tac_toe():
    # Main game loop
    board = create_board()
    current_player = 'X'
    while True:
        print_board(board)
        row, col = get_move(current_player)
        if make_move(board, current_player, row, col):
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
