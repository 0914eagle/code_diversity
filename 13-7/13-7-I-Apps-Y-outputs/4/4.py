
def get_min_moves(a, b):
    if a == b:
        return 0
    if a > b:
        return get_min_moves(a-b, 0)
    else:
        return 1 + get_min_moves(a+b, b)

