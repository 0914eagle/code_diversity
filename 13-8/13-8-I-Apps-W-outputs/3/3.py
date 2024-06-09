
import sys

def solve(n, desks):
    # Initialize the answer as 1
    answer = 1
    
    # Iterate over the desks
    for i in range(n):
        # Get the current and desired desk numbers of the current engineer
        current_desk, desired_desk = desks[i]
        
        # If the current desk is not the desired desk, we have two options:
        # Either move the current engineer to the desired desk and keep the current desk empty, or
        # Move the current engineer to an empty desk and keep the current desk occupied.
        if current_desk != desired_desk:
            answer *= 2
        
        # If the current desk is the desired desk, we can keep it occupied by the current engineer
        
    # Return the answer modulo 1000000007
    return answer % 1000000007

n = int(input())
desks = []

# Iterate over the next n lines of input
for i in range(n):
    # Split the input into the current and desired desk numbers
    current_desk, desired_desk = map(int, input().split())
    
    # Add the current and desired desk numbers to the list of desks
    desks.append((current_desk, desired_desk))

# Call the solve function and print the result
print(solve(n, desks))

