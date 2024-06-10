
import math

def get_expected_severity(bugs, hours, faith_factor):
    
    # Initialize variables
    total_severity = 0
    fixed_bugs = []
    unfixed_bugs = bugs.copy()

    # Loop through the hours
    for hour in range(hours):
        # Choose the bug with the highest probability of fixation
        bug = max(unfixed_bugs, key=lambda x: x[0])

        # Calculate the probability of fixing the bug
        probability = bug[0]

        # Fix the bug with probability equal to the bug's initial probability of fixation
        if math.random() < probability:
            fixed_bugs.append(bug)
            unfixed_bugs.remove(bug)

        # Reduce the probability of fixing the bug if it was not fixed
        else:
            unfixed_bugs.remove(bug)
            unfixed_bugs.append((bug[0] * faith_factor, bug[1]))

    # Calculate the total severity of fixed bugs
    for bug in fixed_bugs:
        total_severity += bug[1]

    return total_severity

def main():
    bugs = []
    hours = int(input())
    faith_factor = float(input())

    for _ in range(hours):
        p, s = map(float, input().split())
        bugs.append((p, s))

    print(get_expected_severity(bugs, hours, faith_factor))

if __name__ == '__main__':
    main()

