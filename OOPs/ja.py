def rook_moves(R, C, X, Y, M, N):
    # Initialize the board with empty squares
    board = [['*' for _ in range(C)] for _ in range(R)]

    # Place the rook and the pawn on the board
    board[X - 1][Y - 1] = 'R'
    board[M - 1][N - 1] = 'P'

    moves = 0

    # Move up
    for i in range(X - 2, -1, -1):
        if board[i][Y - 1] == 'P':
            break
        moves += 1

    # Move down
    for i in range(X, R):
        if board[i][Y - 1] == 'P':
            break
        moves += 1

    # Move left
    for j in range(Y - 2, -1, -1):
        if board[X - 1][j] == 'P':
            break
        moves += 1

    # Move right
    for j in range(Y, C):
        if board[X - 1][j] == 'P':
            break
        moves += 1

    return moves


# Example usage:
if __name__ == "__main__":
    R = 8
    C = 8
    X = 4
    Y = 6
    M = 5
    N = 6

    print(rook_moves(R, C, X, Y, M, N))  # Output should be 11

    R = 5
    C = 6
    X = 2
    Y = 4
    M = 1
    N = 2

    print(rook_moves(R, C, X, Y, M, N))  # Output should be 9
