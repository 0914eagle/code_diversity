
def solve(s, t):
    # Initialize a dictionary to store the number of operations required for each character
    d = {}
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], 0) + 1
        d[t[i]] = d.get(t[i], 0) - 1
    
    # Calculate the total number of operations required
    total = 0
    for key in d:
        total += abs(d[key])
    
    return total

