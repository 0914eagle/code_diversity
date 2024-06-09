
def get_min_keys(n, s):
    # Initialize the number of keys needed to 0
    keys_needed = 0
    
    # Iterate through the string s
    for i in range(0, len(s), 2):
        # If the current position is odd, it represents a key
        if i % 2 == 1:
            # Get the type of the key
            key_type = s[i]
            # Get the type of the door in the next room
            door_type = s[i + 1]
            # If the key type and door type are the same, the key is not needed
            if key_type == door_type:
                keys_needed -= 1
            # Otherwise, the key is needed
            else:
                keys_needed += 1
    
    # Return the minimum number of keys needed
    return keys_needed

