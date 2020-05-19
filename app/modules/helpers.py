def get_valid_moves(piece, player1, player2, checkerboard):
    '''
    :param piece, my_pieces, opponent_pieces, checkerboard: all tuples or tuples[]
    :return: a list of x, y valid moves
    '''
    player1_pieces = player1.get_all_piece_xy()
    player2_pieces = player2.get_all_piece_xy()
    valid_moves = []
    all_pos = checkerboard.get_all_box_xy()
    i = 0
    for pos in all_pos:
        # Target not on another piece
        if pos not in player1_pieces and pos not in player2_pieces:
            # Target on diagonal
            if pos[0] != piece.rect.x and pos[1] != piece.rect.y:
                if abs(pos[0] - piece.rect.x) == abs(pos[1] - piece.rect.y):
                    # Target is black box
                    if checkerboard.get_all_box()[i].color == [100, 100, 100]:
                        # One box distance
                        if abs(pos[0] - piece.rect.x) == 85 and abs(pos[1] - piece.rect.y) == 85:
                            # Remove backward moves
                            if (player1.his_turn and player1.current_user) or (player2.his_turn and player2.current_user):
                                if pos[1] - piece.rect.yplayer2.his_turn and player2.current_user < 0:
                                    valid_moves.append(pos)
                            else:
                                if pos[1] - piece.rect.y > 0:
                                    valid_moves.append(pos)

        i += 1
    return valid_moves

