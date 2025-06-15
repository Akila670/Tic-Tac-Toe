def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    print("=== Tic-Tac-Toe ===")
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter a number (1-9): ")

        if move not in '123456789':
            print("Invalid input. Try again.")
            continue

        row = (int(move)-1) // 3
        col = (int(move)-1) % 3

        if board[row][col] in ['X', 'O']:
            print("Cell already taken. Try another.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break