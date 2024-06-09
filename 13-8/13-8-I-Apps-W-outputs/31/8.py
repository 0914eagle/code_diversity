
def get_happiness(n, m):
    def is_framed_segment(arr, l, r):
        return max(arr[l:r+1]) - min(arr[l:r+1]) == r - l

    def count_framed_segments(arr):
        n = len(arr)
        count = 0
        for l in range(n):
            for r in range(l, n):
                if is_framed_segment(arr, l, r):
                    count += 1
        return count

    def count_happiness(n):
        arr = list(range(1, n+1))
        return count_framed_segments(arr)

    total_happiness = 0
    for perm in permutations(range(1, n+1)):
        total_happiness += count_happiness(n)
        total_happiness %= m

    return total_happiness

