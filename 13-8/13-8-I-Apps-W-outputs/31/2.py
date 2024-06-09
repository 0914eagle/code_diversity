
def permutation_happiness(n, m):
    def is_framed_segment(p, l, r):
        return max(p[l:r+1]) - min(p[l:r+1]) == r - l

    def count_framed_segments(p):
        count = 0
        for l in range(n):
            for r in range(l, n):
                if is_framed_segment(p, l, r):
                    count += 1
        return count

    def count_happiness(p):
        return count_framed_segments(p)

    def count_all_happiness(n, m):
        total_happiness = 0
        for p in permutations(range(1, n+1)):
            total_happiness += count_happiness(p)
            total_happiness %= m
        return total_happiness

    return count_all_happiness(n, m)

