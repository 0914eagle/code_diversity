
def get_emeralds(a, b):
    # Calculate the maximum number of shovels that can be crafted with the given sticks
    max_shovels = a // 2

    # Calculate the maximum number of swords that can be crafted with the given diamonds
    max_swords = b // 2

    # Calculate the maximum number of emeralds that can be earned by crafting shovels and swords
    max_emeralds = max_shovels + max_swords

    return max_emeralds

