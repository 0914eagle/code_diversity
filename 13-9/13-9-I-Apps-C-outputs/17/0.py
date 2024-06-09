
def solve(n, adversaries, dwarves, elves):
    # Sort the elves and dwarves by strength in descending order
    sorted_dwarves = sorted(dwarves, reverse=True)
    sorted_elves = sorted(elves, reverse=True)

    # Create a dictionary to map each elf to its corresponding dwarf
    elf_dwarf_map = {i: adversaries[i-1] for i in range(1, n+1)}

    # Initialize the number of victories to 0
    victories = 0

    # Iterate through the elves and dwarves in descending order
    for elf, dwarf in zip(sorted_elves, sorted_dwarves):
        # If the elf is stronger than the dwarf, they win
        if elf > dwarf:
            victories += 1
        # Otherwise, the dwarf wins
        else:
            break

    return victories

