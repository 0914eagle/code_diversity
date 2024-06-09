
def get_max_victories(N, adversaries, dwarves, elves):
    # Sort the dwarves and elves by strength in descending order
    dwarves = sorted(dwarves, reverse=True)
    elves = sorted(elves, reverse=True)
    
    # Create a dictionary to map each elf to their adversary
    elf_adversary = {i: adversaries[i-1] for i in range(1, N+1)}
    
    # Initialize the number of victories to 0
    victories = 0
    
    # Loop through each elf and their adversary
    for i in range(1, N+1):
        # Find the index of the elf's adversary in the sorted dwarf list
        adj_index = dwarves.index(elf_adversary[i])
        
        # If the elf is stronger than their adversary, they win
        if elves[i-1] > dwarves[adj_index]:
            victories += 1
        
        # Remove the elf's adversary from the list of dwarves
        dwarves.pop(adj_index)
    
    return victories

