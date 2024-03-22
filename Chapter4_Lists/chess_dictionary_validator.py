# Write your code here :-)
chess_dictionary = {'1h': 'bking', '6b': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

alphabet = ['a','b','c','d','e','f','g','h']
bw = ['w', 'b']
pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

chess_spaces = [str(i) + k for i in range(1, 9) for k in alphabet]
chess_pieces = [k + i for i in pieces for k in bw]

def isValidChessBoard (board):
    board_items = board.items()
    board_values = board.values()
    board_keys = board.keys()
    count = {}
    for i, k in board_items:
        count.setdefault(k, 0)
        count[k] = count[k] + 1
    white_pieces = [value for key, value in count.items() if 'w' in key]
    black_pieces = [value for key, value in count.items() if 'b' in key and 'wb' not in key]
    for j in board_keys:
        if j not in chess_spaces:
            return False
    for z in board_values:
        if z not in chess_pieces:
            return False
    if sum(white_pieces) > 16:
        return False
    if sum(black_pieces) > 16:
        return False
    if 'bking' in count:
        if count['bking'] > 1:
            return False
    if 'wking' in count:
        if count['wking'] > 1:
            return False
    if 'bqueen' in count:
        if count['bqueen'] > 1:
            return False
    if 'wqueen' in count:
        if count['wqueen'] > 1:
            return False
    if 'bpawn' in count:
        if count['bpawn'] > 8:
            return False
    if 'wpawn' in count:
        if count['wpawn'] > 8:
            return False
    return True

print(isValidChessBoard(chess_dictionary))
