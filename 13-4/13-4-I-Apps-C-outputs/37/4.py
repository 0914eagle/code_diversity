
import itertools

def get_nth_string(k, n):
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible strings of length k
    for perm in itertools.permutations(list(range(1, k+1))):
        # Check if the string is double free
        if all(perm[i] != perm[i+1] for i in range(len(perm)-1)):
            # Check if the string is k-incremental
            if all(sum(perm[:i+1]) == i*(i+1)//2 for i in range(k)):
                # If both conditions are met, add the string to the list
                strings.append("".join(chr(97 + p) for p in perm))
    
    # Return the nth string in the list, or -1 if it doesn't exist
    return strings[n-1] if n <= len(strings) else -1

