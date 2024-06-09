
def restore_string(n, k, p, q):
    # Initialize a list to store the characters of the string
    s = []
    # Initialize a set to store the unique characters of the string
    unique_chars = set()
    # Loop through the permutation indices
    for i in range(n):
        # If the length of the unique characters list is less than k, add a new character to the string
        if len(unique_chars) < k:
            # Add a new character to the string
            s.append(chr(ord('a') + i))
            # Add the new character to the unique characters set
            unique_chars.add(s[-1])
        # If the length of the unique characters list is greater than or equal to k, add the next character from the permutation
        else:
            # Add the next character from the permutation to the string
            s.append(chr(ord('a') + p[i] - 1))
    # Return the string
    return "".join(s)

