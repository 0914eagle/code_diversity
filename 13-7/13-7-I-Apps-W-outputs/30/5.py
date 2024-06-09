
def solve(s):
    n = len(s)
    permutations = 0
    for i in range(1, n+1):
        permutation = [i] + list(range(1, i)) + list(range(i+1, n+1))
        sequence = [(s[j-1][0], s[j-1][1]) for j in permutation]
        if is_good(sequence):
            permutations += 1
    return permutations % 998244353

def is_good(s):
    first_elements = [pair[0] for pair in s]
    second_elements = [pair[1] for pair in s]
    return not (is_sorted(first_elements) or is_sorted(second_elements))

def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return True
    return False

