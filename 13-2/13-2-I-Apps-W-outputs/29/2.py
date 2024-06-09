
def permutation_happiness(n, m):
    def is_permutation(arr):
        return len(set(arr)) == len(arr) and len(arr) == n

    def is_subsegment(arr, l, r):
        return all(arr[i] in arr[l:r+1] for i in range(l, r+1))

    def is_framed_segment(arr, l, r):
        return max(arr[l:r+1]) - min(arr[l:r+1]) == r - l

    def count_happiness(arr):
        count = 0
        for l in range(1, n+1):
            for r in range(l, n+1):
                if is_subsegment(arr, l, r) and is_framed_segment(arr, l, r):
                    count += 1
        return count

    def count_permutations(n):
        if n == 0:
            return 1
        return n * count_permutations(n-1)

    def count_happiness_modulo(n, m):
        count = 0
        for i in range(count_permutations(n)):
            arr = list(range(1, n+1))
            arr = arr[i:] + arr[:i]
            count += count_happiness(arr)
            count %= m
        return count

    return count_happiness_modulo(n, m)

