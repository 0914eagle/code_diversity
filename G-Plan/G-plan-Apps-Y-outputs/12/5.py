
def find_smallest_integer(numbers):
    return min(numbers)

if __name__ == "__main__":
    input_numbers = list(map(int, input().split()))
    result = find_smallest_integer(input_numbers)
    print(result)
