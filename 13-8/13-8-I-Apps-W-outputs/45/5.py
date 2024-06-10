
def solve(n):
    # Initialize variables
    days = 0
    bacteria = 1
    nights = 0
    split_bacteria = 0
    
    # Loop until the total mass of the bacteria is equal to n
    while bacteria < n:
        # Increment the number of days
        days += 1
        
        # Check if the bacteria can split
        if bacteria > 1:
            # Increment the number of split bacteria
            split_bacteria += 1
            
            # Split the bacteria
            bacteria *= 2
        
        # Increment the number of nights
        nights += 1
        
        # Increment the mass of the bacteria
        bacteria += 1
    
    # Return the minimum number of nights needed and the number of split bacteria
    return nights, split_bacteria

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through the test cases
    for _ in range(t):
        # Read the target mass
        n = int(input())
        
        # Solve the problem
        nights, split_bacteria = solve(n)
        
        # Check if a solution exists
        if nights == -1:
            # Print -1 if no solution exists
            print(-1)
        else:
            # Print the minimum number of nights needed and the number of split bacteria
            print(nights)
            print(" ".join(map(str, split_bacteria)))

if __name__ == '__main__':
    main()

