
def solve(s, t):
    # Initialize a counter for the number of occurrences of t
    count = 0
    
    # Iterate through the characters of s
    for i in range(len(s)):
        # If the current character is a question mark, replace it with a character from t
        if s[i] == "?":
            s = s[:i] + t[i % len(t)] + s[i+1:]
            count += 1
    
    # Return the number of occurrences of t
    return count

