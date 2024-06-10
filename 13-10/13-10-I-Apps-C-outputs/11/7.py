
def get_perfect_square_numbers(numbers):
    perfect_square_numbers = []
    for num in numbers:
        root = num ** 0.5
        if root % 1 == 0:
            perfect_square_numbers.append(num)
    return perfect_square_numbers

def get_largest_non_perfect_square(numbers):
    perfect_square_numbers = get_perfect_square_numbers(numbers)
    largest_non_perfect_square = 0
    for num in numbers:
        if num not in perfect_square_numbers:
            largest_non_perfect_square = max(largest_non_perfect_square, num)
    return largest_non_perfect_square

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_largest_non_perfect_square(numbers))

