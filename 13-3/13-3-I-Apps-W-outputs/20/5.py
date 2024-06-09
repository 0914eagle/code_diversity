
def get_mex(subset):
    subset = set(subset)
    for i in range(len(subset)):
        if i not in subset:
            return i
    return len(subset)

def get_max_mex(numbers):
    numbers = set(numbers)
    max_mex = 0
    for i in range(len(numbers)):
        if i not in numbers:
            max_mex = max(max_mex, i)
    return max_mex

def get_subsets(numbers):
    subsets = []
    for i in range(1 << len(numbers)):
        subset = []
        for j in range(len(numbers)):
            if i & (1 << j):
                subset.append(numbers[j])
        subsets.append(subset)
    return subsets

def get_max_mex_sum(numbers):
    max_mex_sum = 0
    for subset in get_subsets(numbers):
        mex_sum = get_mex(subset) + get_mex(numbers - set(subset))
        max_mex_sum = max(max_mex_sum, mex_sum)
    return max_mex_sum

def get_max_mex_sum_brute_force(numbers):
    max_mex_sum = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            mex_sum = get_mex(numbers[i:j]) + get_mex(numbers[:i] + numbers[j:])
            max_mex_sum = max(max_mex_sum, mex_sum)
    return max_mex_sum

def main():
    tests = int(input())
    for test in range(tests):
        n = int(input())
        numbers = set(map(int, input().split()))
        print(get_max_mex_sum(numbers))

if __name__ == "__main__":
    main()

