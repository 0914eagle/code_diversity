
def get_happiness(n, m):
    def is_framed_segment(p, l, r):
        return max(p[l:r+1]) - min(p[l:r+1]) == r - l

    def count_happiness(p):
        count = 0
        for l in range(1, n+1):
            for r in range(l, n+1):
                if is_framed_segment(p, l, r):
                    count += 1
        return count

    def get_permutations(n):
        if n == 1:
            return [[1]]
        permutations = []
        for p in get_permutations(n-1):
            for i in range(n):
                permutations.append([i+1] + p)
        return permutations

    permutations = get_permutations(n)
    total_happiness = 0
    for p in permutations:
        total_happiness += count_happiness(p)

    return total_happiness % m

