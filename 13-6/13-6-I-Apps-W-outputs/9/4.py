
def get_maximum_sum(numbers):
    # Calculate the sum of the given numbers
    sum_of_numbers = sum(numbers)
    
    # Initialize the maximum sum to be the sum of the given numbers
    maximum_sum = sum_of_numbers
    
    # Loop through each number in the list
    for i in range(len(numbers)):
        # Calculate the sum of the numbers after multiplying the current number by -1
        sum_after_multiplying_by_minus_one = sum_of_numbers - numbers[i]
        
        # If the sum after multiplying the current number by -1 is greater than the maximum sum, update the maximum sum
        if sum_after_multiplying_by_minus_one > maximum_sum:
            maximum_sum = sum_after_multiplying_by_minus_one
    
    # Return the maximum sum
    return maximum_sum

def main():
    # Read the input from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # Call the get_maximum_sum function and print the result
    print(get_maximum_sum(numbers))

if __name__ == '__main__':
    main()

