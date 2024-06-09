
def solve(N, adversaries, dwarves, elves):
    # Sort the dwarves and elves by strength in descending order
    dwarves = sorted(dwarves, reverse=True)
    elves = sorted(elves, reverse=True)
    
    # Create a dictionary to map each dwarf to its strength
    dwarf_strength = {dwarf: strength for dwarf, strength in zip(range(1, N+1), dwarves)}
    
    # Create a dictionary to map each elf to its strength and its chosen adversary
    elf_strength = {elf: (strength, adversary) for elf, strength, adversary in zip(range(1, N+1), elves, adversaries)}
    
    # Initialize the number of victories to 0
    victories = 0
    
    # Iterate through the elves and their chosen adversaries
    for elf, (strength, adversary) in elf_strength.items():
        # If the elf's strength is greater than the adversary's strength, the elf wins
        if strength > dwarf_strength[adversary]:
            victories += 1
        # Otherwise, the adversary wins
        else:
            victories -= 1
    
    # Return the number of victories
    return victories

