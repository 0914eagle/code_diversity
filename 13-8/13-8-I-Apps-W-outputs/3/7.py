
import itertools

def count_seating_arrangements(engineers, desks):
    # Initialize a list to store the possible assignments
    assignments = []
    
    # Iterate over all possible assignments of desks to engineers
    for assignment in itertools.permutations(desks, len(engineers)):
        # Check if the assignment is valid
        if is_valid_assignment(engineers, assignment):
            # Add the valid assignment to the list of possible assignments
            assignments.append(assignment)
    
    # Return the number of possible assignments modulo 1000000007
    return len(assignments) % 1000000007

def is_valid_assignment(engineers, assignment):
    # Check if the assignment is valid by ensuring that no two engineers sit at the same desk
    for i in range(len(engineers)):
        for j in range(i + 1, len(engineers)):
            if assignment[i] == assignment[j]:
                return False
    return True

def main():
    # Read the number of engineers and their current and desired desks from stdin
    num_engineers = int(input())
    engineers = []
    for _ in range(num_engineers):
        current_desk, desired_desk = map(int, input().split())
        engineers.append((current_desk, desired_desk))
    
    # Count the number of possible seating arrangements and print the result
    print(count_seating_arrangements(engineers, range(1, 2 * num_engineers + 1)))

if __name__ == "__main__":
    main()

