
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the number of victories as 0
    victories = 0
    
    # Loop through each elf
    for i in range(N):
        # Find the index of the dwarf that the elf will face
        j = A[i] - 1
        
        # If the elf is stronger than the dwarf, they will win
        if V[i] > P[j]:
            victories += 1
        
        # If the elf is weaker than the dwarf, they will lose
        else:
            pass
    
    # Return the number of victories
    return victories

