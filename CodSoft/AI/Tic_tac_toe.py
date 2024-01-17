# program of tictactoe
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as a list
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
                return True
            return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def minimax(board, depth, maximizing_player, alpha, beta):
    if board.current_winner:
        if maximizing_player:
            return -1
        else:
            return 1
    elif not board.empty_squares():
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, depth + 1, False, alpha, beta)
            board.board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, depth + 1, True, alpha, beta)
            board.board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in board.available_moves():
        board.make_move(move, 'O')
        score = minimax(board, 0, False, float('-inf'), float('inf'))
        board.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.print_board_nums()
    while tic_tac_toe.empty_squares():
        if tic_tac_toe.num_empty_squares() % 2 == 1:
            square = int(input("Enter your move (0-8): "))
            if square not in tic_tac_toe.available_moves():
                print("Invalid move. Try again.")
                continue
            tic_tac_toe.make_move(square, 'X')
        else:
            square = get_best_move(tic_tac_toe)
            tic_tac_toe.make_move(square, 'O')
            print(f"AI makes a move at {square}")
        tic_tac_toe.print_board()
        if tic_tac_toe.current_winner:
            print(f"{tic_tac_toe.current_winner} wins!")
            break
    if not tic_tac_toe.current_winner:
        print("It's a tie!")

if __name__ == "__main__":
    play()
