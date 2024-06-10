
def get_sorted_array(numbers):
    # Your code here
    return sorted(numbers)

def get_min_digit_changes(numbers):
    # Your code here
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    sorted_array = get_sorted_array(numbers)
    min_digit_changes = get_min_digit_changes(numbers)
    print(min_digit_changes)
    for number in sorted_array:
        print(number)

