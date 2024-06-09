
def get_minimum_keys(n, s):
    # Initialize the number of keys needed to be 0
    keys_needed = 0
    
    # Iterate through the string s
    for i in range(0, len(s), 2):
        # If the current position is odd, it means we are at a room with a key
        if i % 2 == 1:
            # Get the type of the key from the string s
            key_type = s[i]
            # Get the type of the door from the string s
            door_type = s[i + 1]
            # If the key type and door type are the same, it means we can open the door without needing a key
            if key_type == door_type:
                continue
            # Otherwise, we need to buy a key of the type that opens the door
            else:
                keys_needed += 1
    
    # Return the minimum number of keys needed to get to the last room
    return keys_needed

