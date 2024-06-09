
def solve(n, p, t, s, e):
    # Initialize the maximum score and the current score
    max_score = 0
    curr_score = 0
    
    # Iterate through each note and check if it is within an SP phrase
    for i in range(n):
        # Check if the note is within an SP phrase
        within_sp = False
        for j in range(p):
            if s[j] <= t[i] <= e[j]:
                within_sp = True
                break
        
        # If the note is within an SP phrase, add two points to the current score
        if within_sp:
            curr_score += 2
        # Otherwise, add one point to the current score
        else:
            curr_score += 1
        
        # Update the maximum score if the current score is higher
        if curr_score > max_score:
            max_score = curr_score
    
    # Return the maximum score
    return max_score

