
def get_coating_length(coating):
    return len(coating)

def get_coating_pieces(coating, t):
    pieces = []
    for i in range(len(coating)):
        for j in range(i+1, len(coating)+1):
            piece = coating[i:j]
            if piece == t:
                return [piece]
            elif piece in pieces:
                continue
            elif t.startswith(piece):
                pieces.append(piece)
    return pieces

def get_coating_pieces_with_order(coating, t):
    pieces = get_coating_pieces(coating, t)
    pieces_with_order = []
    for piece in pieces:
        if piece == t:
            pieces_with_order.append((0, piece))
        else:
            pieces_with_order.append((1, piece))
    return pieces_with_order

def get_coating_needed(coating, t):
    pieces = get_coating_pieces_with_order(coating, t)
    needed_pieces = []
    for piece in pieces:
        if piece not in needed_pieces:
            needed_pieces.append(piece)
    return needed_pieces

def get_coating_needed_length(coating, t):
    pieces = get_coating_needed(coating, t)
    return len(pieces)

def get_coating_needed_pieces(coating, t):
    pieces = get_coating_needed(coating, t)
    return [piece for piece in pieces]

def get_coating_needed_pieces_with_order(coating, t):
    pieces = get_coating_needed(coating, t)
    return [(order, piece) for order, piece in pieces]

def main():
    coating = input("Enter the coating: ")
    t = input("Enter the desired coating: ")
    length = get_coating_length(coating)
    needed_length = get_coating_needed_length(coating, t)
    if length < needed_length:
        print(-1)
    else:
        pieces = get_coating_needed_pieces_with_order(coating, t)
        print(needed_length)
        for order, piece in pieces:
            print(order, piece)

if __name__ == '__main__':
    main()

