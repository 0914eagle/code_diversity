
import sys

def count_assignments(N, current_desks, desired_desks):
    # Initialize a list to store the possible assignments
    assignments = []

    # Iterate over the current and desired desks
    for i in range(N):
        # If the current and desired desks are the same, add the assignment to the list
        if current_desks[i] == desired_desks[i]:
            assignments.append(current_desks[i])
        # If the current and desired desks are different, add both assignments to the list
        else:
            assignments.append(current_desks[i])
            assignments.append(desired_desks[i])

    # Return the number of possible assignments, modulo 1000000007
    return len(set(assignments)) % 1000000007

if __name__ == '__main__':
    N = int(input())
    current_desks = []
    desired_desks = []

    for i in range(N):
        current_desk, desired_desk = map(int, input().split())
        current_desks.append(current_desk)
        desired_desks.append(desired_desk)

    print(count_assignments(N, current_desks, desired_desks))

