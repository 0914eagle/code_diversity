
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for sp in sp_phrases:
            if notes[i] >= sp[0] and notes[i] <= sp[1]:
                # If it is, charge up the SP meter
                current_score += 2
                break
        else:
            # If it's not within an SP phrase, score a regular note
            current_score += 1
        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, current_score)
    
    return max_score

