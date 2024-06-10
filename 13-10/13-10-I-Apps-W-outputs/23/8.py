
def get_maximum_candies(n, k, M, D):
    # Initialize variables
    max_candies = 0
    x = 1
    
    # Iterate through possible values of x
    while x <= M:
        # Calculate the number of candies given to each person
        num_candies = x * k
        
        # Calculate the number of times each person receives candies
        num_times = num_candies // k
        
        # Check if the number of times each person receives candies is less than or equal to D
        if num_times <= D:
            # Calculate the number of candies Arkady receives
            arkady_candies = num_candies - (num_candies % k)
            
            # Update the maximum number of candies if necessary
            if arkady_candies > max_candies:
                max_candies = arkady_candies
        
        # Increment x
        x += 1
    
    # Return the maximum number of candies Arkady can receive
    return max_candies

def main():
    # Read the input
    n, k, M, D = map(int, input().split())
    
    # Call the get_maximum_candies function and print the result
    print(get_maximum_candies(n, k, M, D))

if __name__ == '__main__':
    main()

