def who_is_winner(pieces_position_list):
    board = {col: [] for col in 'ABCDEFG'}
    rows = 6

    def check_winner(color):
        for col in 'ABCDEFG':
            if len(board[col]) >= 4 and all(board[col][i] == color for i in range(-4, 0)):
                return color

        for col in range(7):
            for row in range(rows):
                if (
                    col <= 3 and
                    all(col_name in board and len(board[col_name]) > row and board[col_name][row] == color 
                        for col_name in 'ABCDEFG'[col:col+4])
                ):
                    return color
                if (
                    col <= 3 and row <= 2 and
                    all('ABCDEFG'[col+i] in board and len(board['ABCDEFG'[col+i]]) > row + i and 
                        board['ABCDEFG'[col+i]][row + i] == color 
                        for i in range(4))
                ):
                    return color
                if (
                    col <= 3 and row >= 3 and
                    all('ABCDEFG'[col+i] in board and len(board['ABCDEFG'[col+i]]) > row - i and 
                        board['ABCDEFG'[col+i]][row - i] == color 
                        for i in range(4))
                ):
                    return color

        return None

    for move in pieces_position_list:
        col, color = move.split('_')
        board[col].append(color)
        winner = check_winner(color)
        if winner:
            return winner

    return 'Draw'
