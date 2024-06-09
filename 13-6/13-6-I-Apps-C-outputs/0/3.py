
def get_valid_assignments(n, m, t, op):
    # Initialize a list to store the valid assignments
    valid_assignments = []
    
    # Iterate over all possible assignments of digits in the section
    for assignment in itertools.product(range(1, n+1), repeat=m):
        # Check if the assignment is valid
        if is_valid_assignment(assignment, n, m, t, op):
            # If the assignment is valid, add it to the list of valid assignments
            valid_assignments.append(assignment)
    
    # Return the number of valid assignments
    return len(valid_assignments)

def is_valid_assignment(assignment, n, m, t, op):
    # Initialize a set to store the digits used in the section
    digits = set()
    
    # Iterate over the assignment
    for digit in assignment:
        # Add the digit to the set of used digits
        digits.add(digit)
    
    # Check if all digits are used
    if len(digits) != m:
        return False
    
    # Check if the target value is reached
    if not is_target_reached(assignment, n, m, t, op):
        return False
    
    # Check if the assignment is valid by checking if no digit appears more than once in any row or column
    for i in range(n):
        for j in range(n):
            # If a digit appears more than once in the same row or column, return False
            if assignment[i] in assignment[j:n] or assignment[j] in assignment[i:n]:
                return False
    
    # If all checks pass, return True
    return True

def is_target_reached(assignment, n, m, t, op):
    # Initialize a variable to store the result
    result = 0
    
    # Iterate over the assignment
    for i in range(m):
        # Add the digit to the result
        result += assignment[i]
    
    # Check if the result is equal to the target value
    if result == t:
        return True
    
    # If the result is not equal to the target value, return False
    return False

if __name__ == '__main__':
    n, m, t, op = map(int, input().split())
    print(get_valid_assignments(n, m, t, op))

