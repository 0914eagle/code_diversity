
def solve(N, adversaries, dwarves, elves):
    # Initialize a dictionary to store the strength of each elf
    elf_strength = {}
    for i in range(N):
        elf_strength[i+1] = elves[i]

    # Initialize a dictionary to store the strength of each dwarf
    dwarf_strength = {}
    for i in range(N):
        dwarf_strength[i+1] = dwarves[i]

    # Initialize a dictionary to store the number of victories for each elf
    elf_victories = {}
    for i in range(N):
        elf_victories[i+1] = 0

    # Initialize a list to store the order of elves to send to the hall
    send_order = []

    # Loop through each elf and calculate their strength against each dwarf
    for i in range(N):
        elf = i+1
        adversary = adversaries[i]
        elf_strength[elf] += dwarf_strength[adversary]
        send_order.append(elf)

    # Loop through each elf in the send order and calculate their number of victories
    for elf in send_order:
        victories = 0
        for i in range(N):
            if elf_strength[elf] > elf_strength[i+1]:
                victories += 1
        elf_victories[elf] = victories

    # Return the maximum number of victories
    return max(elf_victories.values())

