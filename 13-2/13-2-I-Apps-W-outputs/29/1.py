
def permutation_happiness(n, m):
    def is_permutation(arr):
        return len(set(arr)) == len(arr) and len(arr) == n

    def is_subsegment(arr, l, r):
        return all(arr[i] != arr[i + 1] for i in range(l, r))

    def is_framed_segment(arr, l, r):
        return max(arr[l:r]) - min(arr[l:r]) == r - l

    def count_happiness(arr):
        count = 0
        for l in range(n):
            for r in range(l, n):
                if is_subsegment(arr, l, r) and is_framed_segment(arr, l, r):
                    count += 1
        return count

    def count_all_permutations(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def count_happiness_modulo(n, m):
        count = 0
        for i in range(count_all_permutations(n)):
            arr = list(range(1, n + 1))
            arr = arr[i:] + arr[:i]
            if is_permutation(arr):
                count += count_happiness(arr)
        return count % m

    return count_happiness_modulo(n, m)

