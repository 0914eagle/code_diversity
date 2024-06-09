
def solve(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for sp in sp_phrases:
            if notes[i] in range(sp[0], sp[1]):
                # If it is, charge up the SP meter
                current_score += 2
        
        # If the current note is not within an SP phrase, score it normally
        else:
            current_score += 1
        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

