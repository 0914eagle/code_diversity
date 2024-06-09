
def get_prepared_chocolate_pieces(n, d, x, a):
    total_pieces = 0
    for i in range(n):
        total_pieces += (d // (a[i] + 1)) * (a[i] + 1)
    return x + total_pieces

