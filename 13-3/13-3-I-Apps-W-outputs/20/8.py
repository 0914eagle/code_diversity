
def get_mex(subset):
    mex = 0
    while mex in subset:
        mex += 1
    return mex

def get_max_mex(numbers):
    max_mex = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                continue
            else:
                max_mex = max(max_mex, get_mex(numbers[i:j+1]))
    return max_mex

def get_subsets(numbers):
    subsets = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                continue
            else:
                subsets.append(numbers[i:j+1])
    return subsets

def get_max_mex_subsets(numbers):
    max_mex = 0
    for subset in get_subsets(numbers):
        max_mex = max(max_mex, get_max_mex(subset))
    return max_mex

def solve(numbers):
    return get_max_mex_subsets(numbers)

