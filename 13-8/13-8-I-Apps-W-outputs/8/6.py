
def get_keys_to_open_chests(chests, keys):
    # Initialize a dictionary to store the keys that can open each chest
    keys_to_open_chests = {}
    
    # Iterate over the keys
    for key in keys:
        # Get the value of the key
        key_value = key[1]
        
        # Iterate over the chests
        for chest in chests:
            # Get the value of the chest
            chest_value = chest[0]
            
            # Check if the sum of the key value and the chest value is odd
            if (key_value + chest_value) % 2 == 1:
                # If it is, add the key to the dictionary with the chest as the key
                keys_to_open_chests[chest] = key
    
    return keys_to_open_chests

def get_maximum_number_of_opened_chests(keys_to_open_chests):
    # Initialize a set to store the opened chests
    opened_chests = set()
    
    # Iterate over the keys to open chests dictionary
    for chest, key in keys_to_open_chests.items():
        # Check if the chest has already been opened
        if chest not in opened_chests:
            # If it hasn't, add the chest to the set of opened chests and the key to the dictionary
            opened_chests.add(chest)
    
    return len(opened_chests)

def main():
    # Read the number of chests and keys
    n, m = map(int, input().split())
    
    # Read the values of the chests
    chests = [list(map(int, input().split())) for _ in range(n)]
    
    # Read the values of the keys
    keys = [list(map(int, input().split())) for _ in range(m)]
    
    # Get the keys that can open each chest
    keys_to_open_chests = get_keys_to_open_chests(chests, keys)
    
    # Get the maximum number of opened chests
    maximum_number_of_opened_chests = get_maximum_number_of_opened_chests(keys_to_open_chests)
    
    # Print the maximum number of opened chests
    print(maximum_number_of_opened_chests)

if __name__ == '__main__':
    main()

