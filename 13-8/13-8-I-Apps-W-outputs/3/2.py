
import sys

def solve(n, desks):
    # Initialize the number of possible assignments to 1
    assignments = 1
    
    # Iterate over the desks
    for i in range(n):
        # Get the current and desired desk numbers for the current engineer
        current_desk, desired_desk = desks[i]
        
        # If the engineer wants to move to a different desk
        if current_desk != desired_desk:
            # Update the number of possible assignments by the number of possible assignments for the current engineer
            assignments *= (n - 1)
            
            # Update the number of possible assignments by the number of possible assignments for the other engineers
            for j in range(n):
                if j != i:
                    assignments *= 2
    
    # Return the number of possible assignments modulo 1000000007 = 10^9 + 7
    return assignments % 1000000007

n = int(input())
desks = []

# Iterate over the number of engineers
for i in range(n):
    # Read the current and desired desk numbers for the current engineer
    current_desk, desired_desk = map(int, input().split())
    
    # Add the current and desired desk numbers to the list of desks
    desks.append((current_desk, desired_desk))

# Call the solve function and print the result
print(solve(n, desks))

