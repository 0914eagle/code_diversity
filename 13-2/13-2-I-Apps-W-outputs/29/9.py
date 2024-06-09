
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

    def count_all_permutations(n):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    def count_happiness_modulo(n, m):
        count = 0
        for perm in range(count_all_permutations(n)):
            arr = [i for i in range(1, n+1)]
            for i in range(n):
                arr[i] = perm // (n-i) % n + 1
                perm %= (n-i)
            count += count_happiness(arr)
        return count % m

    return count_happiness_modulo(n, m)

