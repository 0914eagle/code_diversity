
def get_emeralds(a, b):
    # Calculate the number of shovels that can be crafted with the given sticks and diamonds
    num_shovels = a // 2
    
    # Calculate the number of swords that can be crafted with the given sticks and diamonds
    num_swords = b // 2
    
    # Calculate the total number of tools that can be crafted
    total_tools = num_shovels + num_swords
    
    # Calculate the number of emeralds that can be earned by selling the tools
    num_emeralds = total_tools
    
    return num_emeralds

