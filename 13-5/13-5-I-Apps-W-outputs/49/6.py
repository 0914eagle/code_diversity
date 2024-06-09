
def get_arithmetic_progression(numbers):
    # Sort the numbers in increasing order
    numbers.sort()
    # Calculate the difference between each two consecutive numbers
    differences = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]
    # Check if all differences are equal
    if len(set(differences)) == 1:
        # If all differences are equal, return the common difference
        return differences[0]
    else:
        # If the differences are not equal, return 0
        return 0

def get_missing_number(numbers, common_difference):
    # Calculate the missing number by using the common difference and the last number in the list
    return numbers[-1] + common_difference

def get_all_numbers(numbers, common_difference):
    # Calculate all the numbers in the arithmetic progression by using the common difference and the first number in the list
    return [numbers[0] + i * common_difference for i in range(len(numbers))]

def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    common_difference = get_arithmetic_progression(numbers)
    if common_difference == 0:
        print(-1)
    else:
        missing_number = get_missing_number(numbers, common_difference)
        all_numbers = get_all_numbers(numbers, common_difference)
        print(len(all_numbers) - len(numbers))
        print(*all_numbers)

if __name__ == '__main__':
    main()

