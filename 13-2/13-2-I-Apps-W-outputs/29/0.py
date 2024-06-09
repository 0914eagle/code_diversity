
def permutation_happiness(n, m):
    def is_permutation(arr):
        return len(set(arr)) == len(arr) and len(arr) == n

    def is_subsegment(arr, l, r):
        return all(arr[i] in arr[l:r+1] for i in range(l, r+1))

    def is_framed_segment(arr, l, r):
        return max(arr[l:r+1]) - min(arr[l:r+1]) == r - l

    def count_happiness(arr):
        count = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                if is_subsegment(arr, i, j) and is_framed_segment(arr, i, j):
                    count += 1
        return count

    def count_all_permutations(n):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    def count_happiness_modulo(n, m):
        count = 0
        for i in range(count_all_permutations(n)):
            arr = list(range(1, n+1))
            arr = arr[i:] + arr[:i]
            if is_permutation(arr):
                count += count_happiness(arr)
        return count % m

    return count_happiness_modulo(n, m)

