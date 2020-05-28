import hashlib
import modules.database as db


def get_valid_moves(piece, player1, player2, checkerboard):
    '''
    :param piece, my_pieces, opponent_pieces, checkerboard: all tuples or tuples[]
    :return: a list of x, y valid moves
    '''
    player1.attack_moves = {}
    player2.attack_moves = {}
    player1_pieces = player1.get_all_piece_xy()
    player2_pieces = player2.get_all_piece_xy()
    player = 1 if piece.color == player1.checkerpieces.sprites()[0].color else 2
    valid_moves = []
    all_pos = checkerboard.get_all_box_xy()
    i = 0
    for pos in all_pos:
        VALID = False
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
                            if (player1.his_turn and player1.current_user) or (
                                    player2.his_turn and player2.current_user):
                                if pos[1] - piece.rect.y < 0:
                                    VALID = True
                            else:
                                if pos[1] - piece.rect.y > 0:
                                    VALID = True
                        # 2 boxes diagonal move
                        elif abs(pos[0] - piece.rect.x) == 170 and abs(pos[1] - piece.rect.y) == 170:
                            # If it's an opponent's piece
                            if player == 1:
                                if (piece.rect.x + (pos[0] - piece.rect.x) / 2, piece.rect.y + (pos[1] - piece.rect.y) / 2) in player2_pieces:
                                    VALID = True
                                    player1.attack_moves[(pos[0],pos[1])] = (int(piece.rect.x + (pos[0] - piece.rect.x) / 2), int(piece.rect.y + (pos[1] - piece.rect.y) / 2))
                            else:
                                if (piece.rect.x + (pos[0] - piece.rect.x) / 2, piece.rect.y + (pos[1] - piece.rect.y) / 2) in player1_pieces:
                                    VALID = True
                                    player2.attack_moves[(pos[0],pos[1])] = (int(piece.rect.x + (pos[0] - piece.rect.x) / 2), int(piece.rect.y + (pos[1] - piece.rect.y) / 2))
        if VALID:
            valid_moves.append(pos)

        i += 1
    print(player1.attack_moves)
    return valid_moves


def chiffr(password):
    return hashlib.sha1(password.encode()).hexdigest()


def check_login(username, password):
    user = db.select('username', 'user', f"where username = '{username}' and password = '{chiffr(password)}'")
    print(user)
    return True if user != [] else False


def check_register(username):
    same_user = db.select('username', 'user', f"where username = '{username}'")
    print(same_user)
    return True if same_user == [] else False


def register(username, password):
    db.insert('user (username, password)', (username, chiffr(password)))
