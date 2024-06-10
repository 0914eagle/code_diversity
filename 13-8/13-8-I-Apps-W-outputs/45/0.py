
def get_bacteria_growth(n):
    # Initialize variables
    day = 1
    night = 1
    bacteria = 1
    total_mass = 1
    
    # Loop until the total mass is equal to n
    while total_mass != n:
        # Increment the day and night
        day += 1
        night += 1
        
        # Check if the bacteria can split
        if bacteria >= 2:
            # Split the bacteria into two
            bacteria = bacteria / 2
            
        # Increment the bacteria mass
        bacteria += 1
        
        # Add the bacteria mass to the total mass
        total_mass += bacteria
    
    # Return the day and night needed to reach the total mass
    return [day, night]

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through the test cases
    for _ in range(t):
        # Read the total mass
        n = int(input())
        
        # Call the get_bacteria_growth function
        day, night = get_bacteria_growth(n)
        
        # Check if a solution exists
        if day == 0 and night == 0:
            # Print -1 if no solution exists
            print(-1)
        else:
            # Print the day and night needed to reach the total mass
            print(day)
            print(night)

if __name__ == '__main__':
    main()

