
def solve(a):
    # Convert the input to a string
    a_str = str(a)
    
    # Create a list to store the digits of a
    a_list = []
    
    # Iterate through the digits of a and store them in the list
    for digit in a_str:
        a_list.append(int(digit))
    
    # Initialize a variable to store the result
    result = 0
    
    # Iterate through the permutations of the digits of a
    for perm in permutations(a_list):
        # Convert the permutation to an integer
        perm_int = int("".join(map(str, perm)))
        
        # Check if the permutation is divisible by 7
        if perm_int % 7 == 0:
            # If it is, return the result
            result = perm_int
            break
    
    # If no permutation is divisible by 7, return 0
    if result == 0:
        return 0
    else:
        return result

