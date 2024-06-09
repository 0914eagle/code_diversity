
def solve(s, t):
    n = len(s)
    if n != len(t):
        return "-1"
    
    # Initialize the number of moves to 0
    k = 0
    
    # Loop through each character in s
    for i in range(n):
        # If the characters at the current position and next position are not the same, we can make a move
        if s[i] != t[i]:
            # Increment the number of moves
            k += 1
            # Swap the characters at the current position and next position
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
    
    # Return the number of moves and the positions of the swaps
    return str(k) + "\n" + " ".join(str(i) for i in range(1, n))

