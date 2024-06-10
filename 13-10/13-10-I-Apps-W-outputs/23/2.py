
def solve(n, k, M, D):
    # Initialize variables
    max_candies = 0
    x = 1
    
    # Loop through all possible values of x
    while x <= min(n, M):
        # Calculate the number of candies each person will receive
        candies_per_person = x
        total_candies = 0
        for i in range(k):
            total_candies += candies_per_person
        
        # Check if the number of candies per person is less than or equal to D
        if total_candies // k <= D:
            # Update the maximum number of candies if necessary
            max_candies = max(max_candies, total_candies)
        
        # Increment x
        x += 1
    
    # Return the maximum number of candies
    return max_candies

def main():
    # Read input
    n, k, M, D = map(int, input().split())
    
    # Call the solve function
    max_candies = solve(n, k, M, D)
    
    # Print the result
    print(max_candies)
    
if __name__ == '__main__':
    main()

