
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex

def get_maximum_mex(numbers):
    n = len(numbers)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(numbers[j])
        subsets.append(subset)

    maximum_mex = 0
    for subset in subsets:
        mex_a = get_mex(subset)
        mex_b = get_mex(numbers) - mex_a
        maximum_mex = max(maximum_mex, mex_a + mex_b)

    return maximum_mex

numbers = [0, 2, 1, 5, 0, 1]
print(get_maximum_mex(numbers))

