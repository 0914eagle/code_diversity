
def find_min_difference(k, n):
    n_str = str(n)
    n_len = len(n_str)
    min_diff = n_len + 1
    for i in range(1, n_len + 1):
        diff = 0
        for j in range(n_len):
            if n_str[j] != str(k)[j % len(str(k))]:
                diff += 1
        min_diff = min(min_diff, diff)
    return min_diff

