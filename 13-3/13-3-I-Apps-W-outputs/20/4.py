
def get_mex(subset):
    subset = list(subset)
    subset.sort()
    mex = 0
    for i in range(len(subset)):
        if subset[i] != mex:
            return mex
        mex += 1
    return mex + 1

def get_max_mex(numbers):
    numbers = list(numbers)
    numbers.sort()
    max_mex = 0
    for i in range(len(numbers)):
        subset = numbers[:i] + numbers[i+1:]
        mex = get_mex(subset)
        max_mex = max(max_mex, mex)
    return max_mex

def solve(numbers):
    return get_max_mex(numbers)

