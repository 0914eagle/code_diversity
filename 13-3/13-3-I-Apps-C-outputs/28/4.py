
def solve(n, p, t, s, e):
    # Initialize the maximum score and the current score
    max_score = 0
    curr_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(n):
        # Check if the current note is within an SP phrase
        within_sp = False
        for j in range(p):
            if s[j] <= t[i] <= e[j]:
                within_sp = True
                break
        
        # If the current note is within an SP phrase, activate Star Power
        if within_sp:
            curr_score += 2
        else:
            curr_score += 1
        
        # Update the maximum score
        max_score = max(max_score, curr_score)
    
    return max_score

