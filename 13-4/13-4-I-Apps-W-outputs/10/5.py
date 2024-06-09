
def get_coatings(s, t):
    n = len(t)
    coating_list = []
    for i in range(n):
        coating_list.append(t[i])
    for i in range(n):
        if t[i] in s:
            coating_list.remove(t[i])
    return coating_list
def get_pieces(s, t):
    n = len(t)
    piece_list = []
    for i in range(n):
        piece_list.append(t[i])
    for i in range(n):
        if t[i] in s:
            piece_list.remove(t[i])
    return piece_list
def get_min_coatings(s, t):
    coating_list = get_coatings(s, t)
    piece_list = get_pieces(s, t)
    n = len(coating_list)
    m = len(piece_list)
    if n == 0:
        return -1
    if m == 0:
        return 0
    coating_dict = {}
    for i in range(n):
        coating_dict[coating_list[i]] = 1
    for i in range(m):
        if piece_list[i] in coating_dict:
            coating_dict[piece_list[i]] += 1
    min_coatings = 0
    for key in coating_dict:
        if coating_dict[key] > 1:
            min_coatings += 1
    return min_coatings
def get_pieces_order(s, t):
    coating_list = get_coatings(s, t)
    piece_list = get_pieces(s, t)
    n = len(coating_list)
    m = len(piece_list)
    if n == 0:
        return -1
    if m == 0:
        return 0
    coating_dict = {}
    for i in range(n):
        coating_dict[coating_list[i]] = 1
    for i in range(m):
        if piece_list[i] in coating_dict:
            coating_dict[piece_list[i]] += 1
    pieces_order = []
    for key in coating_dict:
        if coating_dict[key] > 1:
            pieces_order.append(key)
    return pieces_order
def main():
    s = input()
    t = input()
    min_coatings = get_min_coatings(s, t)
    pieces_order = get_pieces_order(s, t)
    print(min_coatings)
    for i in range(len(pieces_order)):
        print(pieces_order[i])
if __name__ == '__main__':
    main()

