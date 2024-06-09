
import sys

def solve(engineers):
    # Initialize the answer as 1
    answer = 1

    # Loop through each engineer
    for engineer in engineers:
        # Get the current and desired desk numbers
        current_desk, desired_desk = engineer

        # If the current and desired desk numbers are different, we can have 2 possibilities:
        # Either the engineer stays at their current desk, or they move to the desired desk.
        # In either case, the answer is multiplied by 2.
        if current_desk != desired_desk:
            answer *= 2

    # Return the answer modulo 1000000007
    return answer % 1000000007

