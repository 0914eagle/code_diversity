
def get_max_hangout_days(n, m, assignments):
    # Sort the assignments in ascending order
    assignments.sort()
    
    # Initialize the maximum number of days Takahashi can hang out
    max_hangout_days = 0
    
    # Iterate over the assignments
    for i in range(m):
        # Calculate the number of days Takahashi can hang out before doing the current assignment
        hangout_days = n - assignments[i]
        
        # Check if Takahashi can hang out for at least one day
        if hangout_days >= 1:
            # Update the maximum number of days Takahashi can hang out
            max_hangout_days = max(max_hangout_days, hangout_days)
    
    # Return the maximum number of days Takahashi can hang out
    return max_hangout_days

def main():
    # Read the input data
    n, m = map(int, input().split())
    assignments = list(map(int, input().split()))
    
    # Calculate the maximum number of days Takahashi can hang out
    max_hangout_days = get_max_hangout_days(n, m, assignments)
    
    # Print the result
    print(max_hangout_days)

if __name__ == '__main__':
    main()

