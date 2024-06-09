
def get_max_sets(n, s):
    max_sets = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == "0":
            max_sets[i] = max_sets[i - 1] + 1
        elif s[i - 1] == "1":
            max_sets[i] = max_sets[i - 1]
        else:
            max_sets[i] = max(max_sets[i - 1], max_sets[i - 2])
    return max_sets

