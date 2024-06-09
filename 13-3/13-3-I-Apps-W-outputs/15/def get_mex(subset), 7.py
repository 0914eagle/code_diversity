
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex


def get_maximum_mex(numbers):
    numbers = list(set(numbers))
    n = len(numbers)
    if n == 0:
        return 0
    if n == 1:
        return numbers[0]

    # sort the numbers in non-decreasing order
    numbers.sort()

    # find the middle index
    mid = n // 2

    # divide the numbers into two subsets
    left = numbers[:mid]
    right = numbers[mid:]

    # find the maximum mex of the two subsets
    mex_left = get_mex(left)
    mex_right = get_mex(right)

    # return the sum of the maximum mex of the two subsets
    return mex_left + mex_right


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(get_maximum_mex(numbers))

