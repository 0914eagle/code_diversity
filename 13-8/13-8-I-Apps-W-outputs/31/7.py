
def happiness(n, m):
    def is_framed_segment(p, l, r):
        return max(p[l:r+1]) - min(p[l:r+1]) == r - l

    def count_happiness(p):
        count = 0
        for l in range(1, n+1):
            for r in range(l, n+1):
                if is_framed_segment(p, l, r):
                    count += 1
        return count

    def count_all_happiness(n):
        total = 0
        for p in permutations(range(1, n+1)):
            total += count_happiness(p)
        return total

    return count_all_happiness(n) % m

