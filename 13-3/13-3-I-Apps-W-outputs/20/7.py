
def get_mex(subset):
    subset = set(subset)
    for i in range(len(subset)):
        if i not in subset:
            return i
    return len(subset)

def get_maximum_mex(numbers):
    numbers = set(numbers)
    maximum = 0
    for i in range(len(numbers)):
        subset = numbers - {i}
        maximum = max(maximum, get_mex(subset))
    return maximum

def solve(numbers):
    numbers = set(numbers)
    maximum = 0
    for i in range(len(numbers)):
        subset = numbers - {i}
        maximum = max(maximum, get_mex(subset) + get_mex(numbers - subset))
    return maximum

if __name__ == "__main__":
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        numbers = set(map(int, input().split()))
        print(solve(numbers))

