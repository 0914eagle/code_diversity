
def get_maximum_victories(dwarves, elves):
    # Sort the dwarves and elves by strength in descending order
    dwarves = sorted(dwarves, reverse=True)
    elves = sorted(elves, reverse=True)
    
    # Initialize the number of victories to 0
    victories = 0
    
    # Iterate through the dwarves and elves together
    for dwarf, elf in zip(dwarves, elves):
        # If the elf is stronger than the dwarf, add 1 to the number of victories
        if elf > dwarf:
            victories += 1
    
    # Return the number of victories
    return victories

