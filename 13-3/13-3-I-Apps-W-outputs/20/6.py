
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

    mid = n // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left_mex = get_mex(left)
    right_mex = get_mex(right)

    left_max = get_max_mex(left)
    right_max = get_max_mex(right)

    if left_mex + right_mex > left_max + right_max:
        return left_mex + right_mex
    else:
        return left_max + right_max


t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_max_mex(numbers))

