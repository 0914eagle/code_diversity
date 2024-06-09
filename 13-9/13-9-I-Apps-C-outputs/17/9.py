
def get_max_victories(N, adversaries, dwarf_strengths, elf_strengths):
    # Sort the dwarf strengths in descending order
    dwarf_strengths.sort(reverse=True)
    # Sort the elf strengths in descending order
    elf_strengths.sort(reverse=True)
    # Initialize the number of victories to 0
    victories = 0
    # Iterate through the elves and dwarves in pairs
    for elf, dwarf in zip(elf_strengths, dwarf_strengths):
        # If the elf is stronger than the dwarf, add 1 to the number of victories
        if elf > dwarf:
            victories += 1
    # Return the number of victories
    return victories

