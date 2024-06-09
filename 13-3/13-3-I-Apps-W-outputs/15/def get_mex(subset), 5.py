
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex

def get_max_mex(numbers):
    numbers = list(set(numbers))
    n = len(numbers)
    if n == 0:
        return 0
    if n == 1:
        return numbers[0]

    # find the middle element
    mid = n // 2
    left = numbers[:mid]
    right = numbers[mid:]

    # find the maximum value of mex(A) + mex(B) for the left and right subsets
    left_mex = get_mex(left)
    right_mex = get_mex(right)
    left_max = get_max_mex(left)
    right_max = get_max_mex(right)

    # return the maximum of the two values
    return max(left_mex + right_max, right_mex + left_max)

def solve(numbers):
    return get_max_mex(numbers)

