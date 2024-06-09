
def get_arithmetic_progression(numbers):
    # Sort the numbers in increasing order
    numbers.sort()
    # Calculate the difference between each two adjacent numbers
    differences = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
    # Check if all differences are equal
    if len(set(differences)) == 1:
        return True
    else:
        return False

def get_missing_number(numbers):
    # Sort the numbers in increasing order
    numbers.sort()
    # Calculate the difference between each two adjacent numbers
    differences = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
    # Calculate the missing number
    missing_number = numbers[0] + differences[0]
    return missing_number

def get_all_numbers(numbers):
    # Sort the numbers in increasing order
    numbers.sort()
    # Calculate the difference between each two adjacent numbers
    differences = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
    # Calculate all the numbers in the arithmetic progression
    all_numbers = [numbers[0] + i * differences[0] for i in range(len(numbers))]
    return all_numbers

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    if get_arithmetic_progression(numbers):
        print(-1)
    else:
        missing_number = get_missing_number(numbers)
        all_numbers = get_all_numbers(numbers)
        print(len(all_numbers))
        print(*all_numbers)

if __name__ == '__main__':
    main()

