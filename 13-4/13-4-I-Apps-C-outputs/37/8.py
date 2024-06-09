
import itertools

def get_nth_string(k, n):
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible strings of length k
    for perm in itertools.permutations('abcdefghijklmnopqrstuvwxyz', k):
        # Check if the string is double free
        if all(perm[i] != perm[i+1] for i in range(len(perm)-1)):
            # Check if the string is k-incremental
            counts = [0] * 26
            for c in perm:
                counts[ord(c) - ord('a')] += 1
            if all(counts[i] == i for i in range(1, k+1)):
                # If both conditions are met, add the string to the list
                strings.append(''.join(perm))
    
    # Return the nth string in the list, or -1 if it doesn't exist
    return strings[n-1] if n <= len(strings) else -1

