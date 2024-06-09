
def solve(s, t):
    # Initialize a dictionary to store the number of operations required for each character
    operations = {}
    for i in range(len(s)):
        operations[s[i]] = i + 1
    
    # Initialize a variable to store the minimum number of operations required
    min_operations = len(s)
    
    # Iterate over the characters of T and check if they are present in S
    for i in range(len(t)):
        if t[i] in operations:
            # If the character is present in S, calculate the number of operations required
            operations_required = len(s) - operations[t[i]] + 1
            # Update the minimum number of operations required if necessary
            min_operations = min(min_operations, operations_required)
    
    return min_operations

