
def bridges_and_islands(a, b, c):
    # Initialize the number of bridges to 0
    num_bridges = 0
    
    # Loop over all possible combinations of bridges
    for i in range(1 << (a + b + c)):
        # Convert the binary representation of the current combination to a list of booleans
        bridge_list = [bool(i & (1 << j)) for j in range(a + b + c)]
        
        # Check if the current combination is valid
        if is_valid_combination(bridge_list, a, b, c):
            # Increment the number of valid combinations
            num_bridges += 1
    
    # Return the number of valid combinations modulo 998 244 353
    return num_bridges % 998244353

def is_valid_combination(bridge_list, a, b, c):
    # Initialize the number of bridges between red and blue islands to 0
    num_red_blue_bridges = 0
    
    # Loop over all possible pairs of red and blue islands
    for i in range(a):
        for j in range(a, a + b):
            # Check if a bridge exists between the current pair of islands
            if bridge_list[i] and bridge_list[j]:
                # Increment the number of bridges between red and blue islands
                num_red_blue_bridges += 1
    
    # Check if the number of bridges between red and blue islands is valid
    if num_red_blue_bridges > 2 or num_red_blue_bridges == 0:
        return False
    
    # Initialize the number of bridges between blue and purple islands to 0
    num_blue_purple_bridges = 0
    
    # Loop over all possible pairs of blue and purple islands
    for i in range(a, a + b):
        for j in range(a + b, a + b + c):
            # Check if a bridge exists between the current pair of islands
            if bridge_list[i] and bridge_list[j]:
                # Increment the number of bridges between blue and purple islands
                num_blue_purple_bridges += 1
    
    # Check if the number of bridges between blue and purple islands is valid
    if num_blue_purple_bridges > 2 or num_blue_purple_bridges == 0:
        return False
    
    # Initialize the number of bridges between red and purple islands to 0
    num_red_purple_bridges = 0
    
    # Loop over all possible pairs of red and purple islands
    for i in range(a):
        for j in range(a + b, a + b + c):
            # Check if a bridge exists between the current pair of islands
            if bridge_list[i] and bridge_list[j]:
                # Increment the number of bridges between red and purple islands
                num_red_purple_bridges += 1
    
    # Check if the number of bridges between red and purple islands is valid
    if num_red_purple_bridges > 2 or num_red_purple_bridges == 0:
        return False
    
    # If all checks pass, return True
    return True

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(bridges_and_islands(a, b, c))

