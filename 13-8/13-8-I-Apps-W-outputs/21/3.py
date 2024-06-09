
def solve(n_1, n_2, k_1, k_2):
    if n_1 <= k_1 and n_2 <= k_2:
        return "First"
    elif n_1 <= k_2 and n_2 <= k_1:
        return "Second"
    else:
        return "First" if n_1 > n_2 else "Second"

