
def solve(n_1, n_2, k_1, k_2):
    if n_1 <= k_1 and n_2 <= k_2:
        return "First"
    if n_1 <= k_2 and n_2 <= k_1:
        return "Second"
    if n_1 <= k_1:
        return "Second"
    if n_2 <= k_2:
        return "First"
    return "First" if n_1 % k_1 == 0 else "Second"

