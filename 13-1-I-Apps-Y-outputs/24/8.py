
def get_total_biscuits(A, B, T):
    total_biscuits = 0
    for i in range(T // A + 1):
        total_biscuits += B
    return total_biscuits

