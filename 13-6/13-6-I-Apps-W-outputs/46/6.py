
def get_min_sum_squares(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the minimum sum of squares to a large value
    min_sum_squares = float('inf')
    
    # Iterate over all possible combinations of numbers
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            # Calculate the sum of the squares of the current combination
            sum_squares = (numbers[i] + numbers[j]) ** 2
            
            # Update the minimum sum of squares if necessary
            if sum_squares < min_sum_squares:
                min_sum_squares = sum_squares
    
    return min_sum_squares

def main():
    # Read the input data
    n = int(input())
    numbers = [int(x) for x in input().split()]
    
    # Solve the problem
    min_sum_squares = get_min_sum_squares(numbers)
    
    # Print the output
    print(min_sum_squares)

if __name__ == '__main__':
    main()

