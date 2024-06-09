
def happiness(n, m):
    def is_permutation(arr):
        return len(set(arr)) == len(arr) and len(arr) == n

    def is_framed_segment(arr, l, r):
        return max(arr[l:r+1]) - min(arr[l:r+1]) == r - l

    def count_happiness(arr):
        count = 0
        for l in range(n):
            for r in range(l, n):
                if is_framed_segment(arr, l, r):
                    count += 1
        return count

    def count_happiness_modulo(n, m):
        total = 0
        for arr in itertools.permutations(range(1, n+1)):
            if is_permutation(arr):
                total += count_happiness(arr)
        return total % m

    return count_happiness_modulo(n, m)

