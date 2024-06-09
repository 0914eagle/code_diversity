
def find_min_difference(k, n):
    n_str = str(n)
    n_len = len(n_str)
    min_diff = n_len + 1
    for i in range(1, n_len + 1):
        n_digits = [int(n_str[j]) for j in range(i)]
        n_sum = sum(n_digits)
        if n_sum >= k:
            min_diff = min(min_diff, i)
    return min_diff

