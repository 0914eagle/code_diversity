
def get_valid_ways(n, m, t, op):
    # Initialize a dictionary to store the valid ways
    valid_ways = {}
    
    # Iterate over each possible assignment of digits
    for assignment in itertools.product(range(1, n+1), repeat=m):
        # Check if the assignment is valid
        if is_valid_assignment(assignment, n, m, t, op):
            # If the assignment is valid, add it to the dictionary
            valid_ways[assignment] = 1
    
    # Return the number of valid ways
    return len(valid_ways)

def is_valid_assignment(assignment, n, m, t, op):
    # Initialize a set to store the digits used in the section
    digits = set()
    
    # Iterate over each grid square in the section
    for i in range(m):
        # Add the digit in the current grid square to the set
        digits.add(assignment[i])
    
    # Check if all digits are unique
    if len(digits) != m:
        return False
    
    # Check if the target value can be reached using the digits and the arithmetic operator
    if not can_reach_target(assignment, n, m, t, op):
        return False
    
    # Check if the assignment is valid for the entire KenKen puzzle
    if not is_valid_puzzle(assignment, n, m):
        return False
    
    # If all checks pass, the assignment is valid
    return True

def can_reach_target(assignment, n, m, t, op):
    # Initialize a set to store the digits used in the section
    digits = set()
    
    # Iterate over each grid square in the section
    for i in range(m):
        # Add the digit in the current grid square to the set
        digits.add(assignment[i])
    
    # Check if the target value can be reached using the digits and the arithmetic operator
    if op == '+':
        return t in digits
    elif op == '-':
        return t - max(digits) in digits
    elif op == '*':
        return t in [a*b for a in digits for b in digits]
    else:
        return t / min(digits) in digits

def is_valid_puzzle(assignment, n, m):
    # Initialize a set to store the digits used in the section
    digits = set()
    
    # Iterate over each grid square in the section
    for i in range(m):
        # Add the digit in the current grid square to the set
        digits.add(assignment[i])
    
    # Check if all digits are unique
    if len(digits) != m:
        return False
    
    # Check if the assignment is valid for the entire KenKen puzzle
    for i in range(n):
        for j in range(n):
            # Check if the current grid square is in the section
            if i >= m or j >= m:
                continue
            
            # Check if the digit in the current grid square is in the set of digits used in the section
            if assignment[i*m+j] not in digits:
                return False
    
    # If all checks pass, the assignment is valid for the entire KenKen puzzle
    return True

if __name__ == '__main__':
    n, m, t, op = map(int, input().split())
    print(get_valid_ways(n, m, t, op))

