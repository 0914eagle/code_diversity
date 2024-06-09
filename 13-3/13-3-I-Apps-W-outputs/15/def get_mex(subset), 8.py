
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex

def get_max_mex(numbers):
    n = len(numbers)
    max_mex = 0
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] == numbers[j]:
                continue
            subset_a = set(numbers[:i] + numbers[i+1:j] + numbers[j+1:])
            subset_b = set(numbers[i:j] + numbers[j:])
            mex_a = get_mex(subset_a)
            mex_b = get_mex(subset_b)
            max_mex = max(max_mex, mex_a + mex_b)
    return max_mex

def solve(numbers):
    return get_max_mex(numbers)

