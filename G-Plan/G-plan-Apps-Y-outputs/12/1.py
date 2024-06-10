
def find_smallest_integer(numbers):
    return min(numbers)

if __name__ == "__main__":
    inputs = list(map(int, input().split()))
    result = find_smallest_integer(inputs)
    print(result)
