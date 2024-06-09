
def solve(n_1, n_2, k_1, k_2):
    if n_1 == 0 or n_2 == 0:
        return "First" if n_1 > n_2 else "Second"
    if k_1 > n_1 or k_2 > n_2:
        return "First"
    return "Second"

