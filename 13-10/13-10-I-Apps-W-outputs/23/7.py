
def get_max_candies(n, k, M, D):
    # Initialize the maximum number of candies that Arkady can receive
    max_candies = 0
    
    # Iterate through all possible values of x
    for x in range(1, min(n, 1000) + 1):
        # Check if x is a valid value of x
        if x <= M and n % x <= D * k:
            # Calculate the number of candies that Arkady can receive with x
            candies = n // x * x
            
            # Update the maximum number of candies if necessary
            max_candies = max(max_candies, candies)
    
    # Return the maximum number of candies that Arkady can receive
    return max_candies

def main():
    # Read the input
    n, k, M, D = map(int, input().split())
    
    # Call the get_max_candies function and print the result
    print(get_max_candies(n, k, M, D))

if __name__ == '__main__':
    main()

