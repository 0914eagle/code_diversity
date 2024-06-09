
def solve(N, adversaries, dwarves, elves):
    # Sort the dwarves and elves by strength
    dwarves = sorted(dwarves)
    elves = sorted(elves)
    
    # Initialize the number of victories to 0
    victories = 0
    
    # Iterate through the elves
    for i in range(N):
        # Find the index of the dwarf that the current elf will fight against
        j = adversaries[i] - 1
        
        # If the current elf is stronger than the dwarf they will fight against
        if elves[i] > dwarves[j]:
            # The current elf wins the duel
            victories += 1
            
            # Remove the current elf and the dwarf they fought against from the lists
            elves.pop(i)
            dwarves.pop(j)
            
            # Since we removed an element from the list, the indices of the elements after the current elf need to be updated
            i -= 1
    
    # Return the number of victories
    return victories

