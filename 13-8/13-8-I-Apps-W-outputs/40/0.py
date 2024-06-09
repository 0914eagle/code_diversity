
def solve(s, t):
    # Initialize a counter for the number of occurrences of t
    count = 0
    
    # Iterate through the string s and check if t is a substring
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            count += 1
    
    # Return the maximum number of occurrences of t
    return count

