
def get_min_amount(N, K, D):
    # Initialize the minimum amount to N
    min_amount = N
    
    # Iterate through all possible amounts
    for i in range(1, N+1):
        # Convert the amount to a string
        amount_str = str(i)
        
        # Check if the amount contains any disliked digits
        if any(digit in amount_str for digit in D):
            continue
        
        # If the amount does not contain any disliked digits, compare it with the current minimum amount
        if i < min_amount:
            min_amount = i
    
    return min_amount

def main():
    # Read the input from stdin
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    
    # Call the function to get the minimum amount
    min_amount = get_min_amount(N, K, D)
    
    # Print the result
    print(min_amount)

if __name__ == '__main__':
    main()

