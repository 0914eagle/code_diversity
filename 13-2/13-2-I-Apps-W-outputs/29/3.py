
def get_happiness(n, m):
    def is_framed_segment(p):
        min_val = p[0]
        max_val = p[0]
        for i in range(1, len(p)):
            if p[i] < min_val:
                min_val = p[i]
            elif p[i] > max_val:
                max_val = p[i]
        return max_val - min_val == len(p) - 1

    def get_happiness_helper(p, i, j):
        if i == j:
            return 1 if is_framed_segment(p[i:j+1]) else 0
        mid = (i + j) // 2
        return get_happiness_helper(p, i, mid) + get_happiness_helper(p, mid+1, j)

    def get_happiness_sum(p):
        return get_happiness_helper(p, 0, len(p)-1)

    permutations = list(itertools.permutations(range(1, n+1)))
    return sum(get_happiness_sum(p) for p in permutations) % m

