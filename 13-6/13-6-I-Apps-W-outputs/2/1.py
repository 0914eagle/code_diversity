
def get_max_finished_sets(n, s):
    max_sets = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == "?":
            continue
        if s[i - 1] == "0":
            max_sets[i] = max_sets[i - 1]
        else:
            max_sets[i] = max_sets[i - 1] + 1
    return max_sets

