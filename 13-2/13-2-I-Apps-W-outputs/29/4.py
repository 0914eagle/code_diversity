
def permutation_happiness(n, m):
    def is_permutation(arr):
        return len(set(arr)) == len(arr) and len(arr) == n

    def is_subsegment(arr, l, r):
        return all(arr[i] in arr[l:r+1] for i in range(l, r+1))

    def is_framed_segment(arr, l, r):
        return max(arr[l:r+1]) - min(arr[l:r+1]) == r - l

    def get_happiness(arr):
        happiness = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                if is_subsegment(arr, i, j) and is_framed_segment(arr, i, j):
                    happiness += 1
        return happiness

    def get_all_permutations(n):
        if n == 1:
            return [[1]]
        permutations = []
        for i in range(1, n+1):
            for perm in get_all_permutations(n-1):
                permutations.append([i] + perm)
        return permutations

    all_permutations = get_all_permutations(n)
    return sum(get_happiness(p) % m for p in all_permutations) % m

