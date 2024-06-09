
import itertools

def solve(s):
    # Generate all possible strings of length len(s) using the letters of s
    candidate_strings = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=len(s))
    
    # Filter out the strings that contain the letters 'w' or 'm'
    filtered_strings = filter(lambda x: 'w' not in x and 'm' not in x, candidate_strings)
    
    # Count the number of strings that are equal to the given string s
    count = sum(1 for string in filtered_strings if string == tuple(s))
    
    return count % (10**9 + 7)

