
def solve(n, pattern):
    # Initialize a set to store all valid IDs
    valid_ids = set()
    
    # Iterate through all possible IDs of length n
    for i in range(2**n):
        # Convert the integer i to a binary string of length n
        id_str = bin(i)[2:].zfill(n)
        
        # Check if the ID satisfies the pattern
        if satisfies_pattern(id_str, pattern):
            # If it does, add it to the set of valid IDs
            valid_ids.add(id_str)
    
    # Return the number of valid IDs
    return len(valid_ids)

def satisfies_pattern(id_str, pattern):
    # If the length of the ID is not equal to the length of the pattern, return False
    if len(id_str) != len(pattern):
        return False
    
    # Initialize a counter to keep track of the number of 1s in the ID
    count = 0
    
    # Iterate through the characters of the ID and the pattern
    for i in range(len(id_str)):
        # If the character in the ID is 1 and the character in the pattern is 1, increment the counter
        if id_str[i] == "1" and pattern[i] == "1":
            count += 1
        # If the character in the ID is 0 and the character in the pattern is *, return True
        elif id_str[i] == "0" and pattern[i] == "*":
            return True
    
    # If the counter is greater than or equal to half the length of the ID, return True
    return count >= len(id_str) // 2

