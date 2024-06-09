
def solve(s):
    # Initialize the score to 0
    score = 0
    
    # Iterate through the string s
    for i in range(len(s)):
        # If the i-th character in s is 'g', play 'p'
        if s[i] == 'g':
            score += 1
        # If the i-th character in s is 'p', play 'g'
        elif s[i] == 'p':
            score -= 1
    
    # Return the maximum possible score, which is 0
    return score

