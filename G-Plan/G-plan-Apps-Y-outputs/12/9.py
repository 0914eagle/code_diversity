
def find_smallest_integer(numbers):
    return min(numbers)

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    result = find_smallest_integer(numbers)
    print(result)
