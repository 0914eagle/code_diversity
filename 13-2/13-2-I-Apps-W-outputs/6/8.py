
def solve(s):
    # Initialize the score to 0
    score = 0
    
    # Iterate through the string s
    for i in range(len(s)):
        # If the i-th character is 'g', play 'p' to win
        if s[i] == 'g':
            score += 1
        # If the i-th character is 'p', play 'g' to win
        elif s[i] == 'p':
            score -= 1
    
    # Return the maximum possible score
    return score

