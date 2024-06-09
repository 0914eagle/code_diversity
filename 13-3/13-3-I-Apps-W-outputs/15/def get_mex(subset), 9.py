
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

    # sort the numbers in non-decreasing order
    numbers.sort()

    # find the midpoint of the list
    mid = n // 2

    # find the mex of the first subset
    subset_a = numbers[:mid]
    mex_a = get_mex(subset_a)

    # find the mex of the second subset
    subset_b = numbers[mid:]
    mex_b = get_mex(subset_b)

    # return the maximum of the two mex values
    return max(mex_a, mex_b)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(get_max_mex(numbers))

