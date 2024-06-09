
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the number of victories as 0
    victories = 0
    
    # Loop through each elf and determine their opponent and strength
    for i in range(N):
        # Find the index of the dwarf with the same label as the elf's adversary
        opponent = A[i] - 1
        
        # If the elf's strength is greater than their opponent's strength, they win
        if V[i] > P[opponent]:
            victories += 1
    
    # Return the number of victories
    return victories

