def get_valid_moves(piece, my_pieces, opponent_pieces, checkerboard):
    '''
    :param piece, my_pieces, opponent_pieces, checkerboard: all tuples or tuples[]
    :return: a list of x, y valid moves
    '''
    valid_moves = []
    all_pos = checkerboard.get_all_box_xy()
    i = 0
    for pos in all_pos:
        # Target not on another piece
        if pos not in my_pieces and pos not in opponent_pieces:
            # Target on diagonal
            if pos[0] != piece.rect.x and pos[1] != piece.rect.y:
                if abs(pos[0] - piece.rect.x) == abs(pos[1] - piece.rect.y):
                    # Target is black box
                    if checkerboard.get_all_box()[i].color == [100, 100, 100]:
                        # One box distance
                        if abs(pos[0] - piece.rect.x) == 85 and abs(pos[1] - piece.rect.y) == 85:
                            valid_moves.append(pos)
        i += 1
    return valid_moves

