
def get_happiness(n, m):
    def is_framed_segment(p):
        max_val = p[0]
        min_val = p[0]
        for i in range(1, len(p)):
            if p[i] > max_val:
                max_val = p[i]
            if p[i] < min_val:
                min_val = p[i]
        return max_val - min_val == len(p) - 1

    def get_happiness_helper(p):
        happiness = 0
        for i in range(len(p)):
            for j in range(i+1, len(p)+1):
                if is_framed_segment(p[i:j]):
                    happiness += 1
        return happiness

    def get_permutations(n):
        if n == 1:
            return [[1]]
        permutations = []
        for i in range(1, n+1):
            for p in get_permutations(n-1):
                permutations.append([i] + p)
        return permutations

    permutations = get_permutations(n)
    happiness = 0
    for p in permutations:
        happiness += get_happiness_helper(p)

    return happiness % m

