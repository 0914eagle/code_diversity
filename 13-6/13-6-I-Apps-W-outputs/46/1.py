
def get_min_sum_of_squares(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the minimum sum of squares to a large value
    min_sum_of_squares = float('inf')
    # Iterate over all possible ways to divide the numbers into groups
    for i in range(1, len(numbers)):
        # Get the sum of the numbers in the current group
        current_sum = sum(numbers[:i])
        # Get the sum of the squares of the numbers in the current group
        current_sum_of_squares = sum([x**2 for x in numbers[:i]])
        # Get the sum of the numbers in the next group
        next_sum = sum(numbers[i:])
        # Get the sum of the squares of the numbers in the next group
        next_sum_of_squares = sum([x**2 for x in numbers[i:]])
        # Calculate the total sum of squares as the sum of the squares of the numbers in the current group plus the sum of the squares of the numbers in the next group
        total_sum_of_squares = current_sum_of_squares + next_sum_of_squares
        # If the total sum of squares is less than the minimum sum of squares, update the minimum sum of squares
        if total_sum_of_squares < min_sum_of_squares:
            min_sum_of_squares = total_sum_of_squares
    # Return the minimum sum of squares
    return min_sum_of_squares

def main():
    # Read the input data
    n = int(input())
    numbers = [int(x) for x in input().split()]
    # Calculate the minimum sum of squares
    min_sum_of_squares = get_min_sum_of_squares(numbers)
    # Print the result
    print(min_sum_of_squares)

if __name__ == '__main__':
    main()

