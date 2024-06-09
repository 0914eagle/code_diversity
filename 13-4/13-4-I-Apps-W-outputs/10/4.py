
def get_coating_length(coating):
    return len(coating)

def get_coating_pieces(coating, target_coating):
    pieces = []
    for i in range(get_coating_length(coating)):
        for j in range(i+1, get_coating_length(coating)+1):
            piece = coating[i:j]
            if piece == target_coating:
                return [i, j]
            elif piece == target_coating[::-1]:
                return [j, i]
    return None

def get_min_coatings_needed(coating, target_coating):
    pieces = get_coating_pieces(coating, target_coating)
    if pieces is None:
        return -1
    else:
        return len(pieces)

def get_coating_pieces_order(coating, target_coating):
    pieces = get_coating_pieces(coating, target_coating)
    if pieces is None:
        return None
    else:
        return pieces

if __name__ == '__main__':
    coating = input()
    target_coating = input()
    print(get_min_coatings_needed(coating, target_coating))
    pieces = get_coating_pieces_order(coating, target_coating)
    if pieces is not None:
        for piece in pieces:
            print(piece[0], piece[1])

