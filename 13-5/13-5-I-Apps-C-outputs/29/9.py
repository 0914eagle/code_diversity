
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the number of victories to 0
    victories = 0
    
    # Iterate through the elves and dwarves in pairs
    for i in range(N):
        # Find the index of the dwarf that the elf will face
        j = A[i] - 1
        
        # If the elf is stronger than the dwarf, they win
        if V[i] > P[j]:
            victories += 1
        
    # Return the number of victories
    return victories
