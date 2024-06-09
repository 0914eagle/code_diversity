
def solve(s):
    # Initialize the score to 0
    score = 0
    
    # Iterate through the string s
    for i in range(len(s)):
        # If the i-th character in s is 'g', play 'p' to maximize the score
        if s[i] == 'g':
            score += 1
        # If the i-th character in s is 'p', play 'g' to minimize the score
        else:
            score -= 1
    
    # Return the maximum possible score
    return score

