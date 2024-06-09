
def solve(A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the number of victories as 0
    victories = 0
    
    # Loop through each elf
    for i in range(len(A)):
        # Find the index of the dwarf that the elf will face
        j = A[i] - 1
        
        # If the elf is stronger than the dwarf, add a victory
        if V[i] > P[j]:
            victories += 1
    
    # Return the number of victories
    return victories
