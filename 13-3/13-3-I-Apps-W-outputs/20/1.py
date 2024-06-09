
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex


def get_max_mex(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    max_mex = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            subset1 = numbers[i:j]
            subset2 = numbers[:i] + numbers[j:]
            mex1 = get_mex(subset1)
            mex2 = get_mex(subset2)
            max_mex = max(max_mex, mex1 + mex2)
    return max_mex


if __name__ == "__main__":
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(get_max_mex(numbers))

