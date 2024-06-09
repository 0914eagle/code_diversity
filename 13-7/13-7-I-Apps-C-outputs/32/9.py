
def solve(n, k, x, rangers):
    # Sort the rangers in increasing order of strength
    rangers.sort()
    
    # Perform the operation k times
    for i in range(k):
        # Take the bitwise XOR of each alternate ranger with x and update its strength
        for j in range(0, n, 2):
            rangers[j] = rangers[j] ^ x
    
    # Return the maximum and minimum strength of the rangers after performing the operation k times
    return max(rangers), min(rangers)

