
def get_minimum_keys(n, s):
    # Initialize the number of keys needed to be 0
    keys_needed = 0
    
    # Iterate through the string s
    for i in range(0, len(s), 2):
        # If the current position is an odd position, it represents a key
        if i % 2 == 1:
            # Get the type of the key
            key_type = s[i]
            # Get the type of the door in the next room
            door_type = s[i + 1]
            # If the key type and door type are the same, we don't need to buy a key
            if key_type == door_type:
                continue
            # Otherwise, we need to buy a key
            keys_needed += 1
    
    return keys_needed

