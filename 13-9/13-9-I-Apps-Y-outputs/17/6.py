
def get_largest_integer_that_can_be_bought(A, B, X):
    # Initialize a list to store the prices of the integers
    prices = []
    
    # Loop through the integers from 1 to 10^9
    for i in range(1, 10**9 + 1):
        # Calculate the price of the current integer
        price = A * i + B * len(str(i))
        
        # If the price is less than or equal to X, add the integer to the list of prices
        if price <= X:
            prices.append(i)
    
    # If the list of prices is empty, return 0
    if not prices:
        return 0
    
    # Return the largest integer that can be bought
    return max(prices)

def main():
    # Read the input from stdin
    A, B, X = map(int, input().split())
    
    # Call the function to get the largest integer that can be bought
    largest_integer = get_largest_integer_that_can_be_bought(A, B, X)
    
    # Print the result
    print(largest_integer)

if __name__ == '__main__':
    main()

