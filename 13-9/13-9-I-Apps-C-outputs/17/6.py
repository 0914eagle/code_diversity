
def solve(n, adversaries, dwarves, elves):
    # Sort the dwarves and elves by strength
    dwarves = sorted(dwarves)
    elves = sorted(elves, reverse=True)
    
    # Create a dictionary to map each elf to its adversary
    elf_adversary = {i: adversaries[i-1] for i in range(1, n+1)}
    
    # Initialize the number of victories to 0
    victories = 0
    
    # Loop through each elf
    for i in range(1, n+1):
        # Find the index of the elf's adversary in the sorted dwarve list
        adj_index = dwarves.index(elf_adversary[i])
        
        # If the elf is stronger than their adversary, they win
        if elves[i-1] > dwarves[adj_index]:
            victories += 1
        
        # Remove the elf and their adversary from the sorted lists
        dwarves.pop(adj_index)
        elves.pop(i-1)
    
    # Return the number of victories
    return victories

