
import sys

def get_number_of_assignments(n, assignments):
    # Initialize a set to store the current and desired desks
    current_desks = set()
    desired_desks = set()
    
    # Loop through the assignments and add the current and desired desks to the sets
    for assignment in assignments:
        current_desks.add(assignment[0])
        desired_desks.add(assignment[1])
    
    # Initialize a variable to store the number of assignments
    num_assignments = 0
    
    # Loop through the possible assignments
    for current_desk in current_desks:
        for desired_desk in desired_desks:
            # Check if the current desk and desired desk are different and if the desired desk is not already occupied
            if current_desk != desired_desk and desired_desk not in current_desks:
                num_assignments += 1
    
    # Return the number of assignments modulo 1000000007
    return num_assignments % 1000000007

n = int(input())
assignments = []
for i in range(n):
    current_desk, desired_desk = map(int, input().split())
    assignments.append((current_desk, desired_desk))
print(get_number_of_assignments(n, assignments))

