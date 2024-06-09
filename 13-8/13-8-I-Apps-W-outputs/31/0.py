
def solve(n, m):
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

    def count_all_permutations(n, m):
        return pow(n, n, m)

    def count_happiness_modulo(n, m):
        count = 0
        for i in range(count_all_permutations(n, m)):
            arr = list(range(1, n+1))
            arr = arr[i:] + arr[:i]
            if is_permutation(arr):
                count += count_happiness(arr)
        return count % m

    return count_happiness_modulo(n, m)

