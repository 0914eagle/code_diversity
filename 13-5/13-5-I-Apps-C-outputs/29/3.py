
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the variables
    victories = 0
    elves = []
    dwarves = []
    
    # Loop through each elf and determine their opponent and victory status
    for i in range(N):
        # Find the opponent for the current elf
        opponent = A[i] - 1
        
        # Check if the elf has already won a duel
        if opponent in dwarves:
            victories += 1
        
        # Add the elf and their opponent to the respective lists
        elves.append(V[i])
        dwarves.append(P[opponent])
    
    # Return the number of victories
    return victories

