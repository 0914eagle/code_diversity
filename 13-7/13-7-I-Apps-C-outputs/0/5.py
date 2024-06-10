
import math

def get_expected_severity(bugs, hours, faith_factor):
    # Initialize the variables
    total_severity = 0
    fixed_bugs = []
    unfixed_bugs = bugs[:]

    # Loop through the hours
    for hour in range(hours):
        # Choose the bug to work on
        bug = choose_bug(unfixed_bugs)

        # Fix the bug with probability p
        if fix_bug(bug, faith_factor):
            # Add the severity of the fixed bug to the total severity
            total_severity += bug[1]

            # Remove the bug from the list of unfixed bugs
            unfixed_bugs.remove(bug)

            # Add the fixed bug to the list of fixed bugs
            fixed_bugs.append(bug)

    # Return the expected total severity
    return total_severity

def choose_bug(bugs):
    # Choose a bug randomly from the list of unfixed bugs
    return bugs[int(math.floor(random.random() * len(bugs)))]

def fix_bug(bug, faith_factor):
    # Fix the bug with probability p
    return random.random() < bug[0] * faith_factor

if __name__ == '__main__':
    # Read the input
    B, T, f = map(int, input().split())
    bugs = []
    for _ in range(B):
        p, s = map(float, input().split())
        bugs.append((p, s))

    # Calculate the expected total severity
    expected_severity = get_expected_severity(bugs, T, f)

    # Print the result
    print(expected_severity)

