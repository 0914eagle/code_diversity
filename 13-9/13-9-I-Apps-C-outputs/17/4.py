
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the number of victories
    victories = 0
    
    # Iterate through the elves
    for i in range(N):
        # Find the index of the dwarf that the elf will fight against
        j = A[i] - 1
        
        # If the elf is stronger than the dwarf, they will win
        if V[i] > P[j]:
            victories += 1
        
        # Remove the defeated dwarf from the list
        P.pop(j)
    
    # Return the number of victories
    return victories

