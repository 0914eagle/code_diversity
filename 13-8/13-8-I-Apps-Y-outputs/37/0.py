
def get_min_amount(N, K, disliked_digits):
    # Initialize a list to store the minimum amount of money
    min_amount = []
    
    # Iterate through the disliked digits
    for digit in disliked_digits:
        # Check if the digit is not in the minimum amount
        if digit not in min_amount:
            # Add the digit to the minimum amount
            min_amount.append(digit)
    
    # Sort the minimum amount in ascending order
    min_amount.sort()
    
    # Initialize a variable to store the current amount
    current_amount = 0
    
    # Iterate through the minimum amount
    for digit in min_amount:
        # Check if the current amount is less than or equal to N
        if current_amount <= N:
            # Add the digit to the current amount
            current_amount = current_amount * 10 + digit
    
    # Return the current amount
    return current_amount

def main():
    # Read the input from stdin
    N, K = map(int, input().split())
    disliked_digits = list(map(int, input().split()))
    
    # Call the get_min_amount function and print the result
    print(get_min_amount(N, K, disliked_digits))

if __name__ == '__main__':
    main()

