
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the variables
    victories = 0
    elves = []
    dwarves = []
    
    # Loop through each elf and dwarf
    for i in range(N):
        # Add the elf to the list of elves
        elves.append(V[i])
        # Add the dwarf to the list of dwarves
        dwarves.append(P[A[i]-1])
    
    # Sort the elves and dwarves by strength in descending order
    elves = sorted(elves, reverse=True)
    dwarves = sorted(dwarves, reverse=True)
    
    # Loop through each elf and dwarf
    for i in range(N):
        # Check if the elf is stronger than the dwarf
        if elves[i] > dwarves[i]:
            # Increment the number of victories
            victories += 1
    
    # Return the number of victories
    return victories

