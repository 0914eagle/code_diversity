
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex


def get_max_mex(numbers):
    subsets = []
    for i in range(len(numbers)):
        subset = numbers[:i] + numbers[i+1:]
        subsets.append(subset)
    return max(get_mex(subset) for subset in subsets)


def solve(numbers):
    return get_max_mex(numbers)


if __name__ == "__main__":
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        numbers = list(map(int, input().split()))
        print(solve(numbers))

