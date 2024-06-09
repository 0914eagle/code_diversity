
def get_min_keys(n, s):
    # Initialize the number of keys needed to be bought
    keys_needed = 0
    # Iterate through the string s
    for i in range(0, len(s), 2):
        # If the current position is an odd position
        if i % 2 == 1:
            # Get the type of the key from the string s
            key_type = s[i]
            # Get the type of the door from the string s
            door_type = s[i + 1]
            # If the key type and door type are the same
            if key_type == door_type:
                # Increment the number of keys needed
                keys_needed += 1
    # Return the minimum number of keys needed
    return keys_needed

