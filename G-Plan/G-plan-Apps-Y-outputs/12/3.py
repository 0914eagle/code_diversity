
def find_smallest_integer(integers):
    return min(integers)

if __name__ == "__main__":
    input_values = list(map(int, input().split()))
    result = find_smallest_integer(input_values)
    print(result)
