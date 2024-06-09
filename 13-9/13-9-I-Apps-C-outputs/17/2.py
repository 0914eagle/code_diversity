
def solve(N, A, P, V):
    # Sort the dwarves and elves by strength in descending order
    P = sorted(P, reverse=True)
    V = sorted(V, reverse=True)
    
    # Initialize the number of victories for each elf
    victories = [0] * N
    
    # Iterate through each elf
    for i in range(N):
        # Find the strongest dwarf that is not yet defeated
        j = 0
        while j < N and victories[A[i]-1] > 0:
            j += 1
            j = j % N
        
        # Update the number of victories for the current elf
        if P[j] > V[i]:
            victories[i] += 1
        else:
            victories[A[i]-1] += 1
    
    # Return the maximum number of victories
    return max(victories)

