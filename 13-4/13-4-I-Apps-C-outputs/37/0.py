
import itertools

def get_nth_string(k, n):
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible strings of length k
    for perm in itertools.permutations(list(range(1, k+1))):
        # Convert the permutation to a string
        string = "".join(chr(ord('a') + p - 1) for p in perm)
        
        # Check if the string is double free
        if all(string[i] != string[i+1] for i in range(len(string) - 1)):
            # Check if the string is k-incremental
            if all(string.count(chr(ord('a') + i - 1)) == i for i in range(1, k+1)):
                # If both conditions are met, add the string to the list
                strings.append(string)
    
    # Return the nth string in the list, or -1 if it doesn't exist
    return strings[n-1] if n <= len(strings) else -1

