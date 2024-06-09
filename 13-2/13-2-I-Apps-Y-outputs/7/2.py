
import itertools

def get_smallest_string(s, t):
    # Create a list of all possible strings that satisfy Condition 1
    possible_strings = [s[i:i+len(t)] for i in range(len(s)-len(t)+1)]
    
    # Filter out strings that do not contain T as a contiguous substring
    possible_strings = [s for s in possible_strings if t in s]
    
    # Sort the list of possible strings lexicographically
    possible_strings.sort()
    
    # Return the first string in the list, which is the lexicographically smallest string that satisfies Condition 1
    if possible_strings:
        return possible_strings[0]
    else:
        return "UNRESTORABLE"

s = input()
t = input()
print(get_smallest_string(s, t))

