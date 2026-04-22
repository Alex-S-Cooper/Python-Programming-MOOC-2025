# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if not x in [0, 1, 2] or not y in [0, 1, 2]:
        return False
    elif game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False
    

