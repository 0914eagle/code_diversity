
def solve(a, b, l, r):
    # Initialize the string with the first a letters of the alphabet
    s = "".join(chr(i + ord('a')) for i in range(a))
    
    # Initialize the number of different letters in the segment
    num_diff_letters = a
    
    # Iterate through each letter added by Mister B
    for i in range(b):
        # Get the suffix of length a from the current string
        suffix = s[-a:]
        
        # Generate a new string of length a with distinct letters not in the suffix
        t = "".join(chr(i + ord('a')) for i in range(a) if chr(i + ord('a')) not in suffix)
        
        # Append the new string to the end of the current string
        s += t
        
        # Update the number of different letters in the segment
        num_diff_letters = min(num_diff_letters, len(set(s[l-1:r])))
    
    # Return the minimum number of different letters in the segment
    return num_diff_letters

