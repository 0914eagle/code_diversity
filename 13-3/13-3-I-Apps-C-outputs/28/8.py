
def solve(n, p, t, s, e):
    # Initialize the maximum score and the current score
    max_score = 0
    curr_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(n):
        # Check if the current note is within an SP phrase
        for j in range(p):
            if s[j] <= t[i] <= e[j]:
                # If the note is within an SP phrase, activate Star Power
                curr_score += 2
                break
        else:
            # If the note is not within an SP phrase, score it normally
            curr_score += 1
    
    # Update the maximum score if the current score is higher
    max_score = max(max_score, curr_score)
    
    return max_score

