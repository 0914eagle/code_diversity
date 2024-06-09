
def solve(n, P):
    # Convert the pattern P to a list of 1s and *s
    pattern = [1 if x == "1" else 0 for x in P]
    
    # Initialize the maximum number of members to 0
    max_members = 0
    
    # Iterate over all possible IDs
    for i in range(2**n):
        # Convert the current ID to a binary string
        id_str = bin(i)[2:]
        id_str = "0" * (n - len(id_str)) + id_str
        
        # Check if the current ID satisfies the pattern
        if satisfies_pattern(id_str, pattern):
            max_members += 1
    
    return max_members

def satisfies_pattern(id_str, pattern):
    # Check if the length of the ID is equal to the length of the pattern
    if len(id_str) != len(pattern):
        return False
    
    # Check if the ID satisfies the pattern
    for i in range(len(id_str)):
        if pattern[i] == 1 and id_str[i] != "1":
            return False
    
    return True

