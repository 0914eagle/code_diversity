
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    curr_score = 0
    
    # Initialize the SP meter and the SP activation flag
    sp_meter = 0
    sp_activated = False
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for j in range(len(sp_phrases)):
            if notes[i] >= sp_phrases[j][0] and notes[i] <= sp_phrases[j][1]:
                # If the current note is within an SP phrase, activate the SP meter
                sp_meter += 1
                sp_activated = True
                break
        
        # If the SP meter is positive and the current note is within the activation time, score double points
        if sp_meter > 0 and sp_activated:
            curr_score += 2
        else:
            # If the SP meter is not positive or the current note is not within the activation time, score single points
            curr_score += 1
        
        # If the current note is the last note of an SP phrase, deactivate the SP meter
        if i == len(notes) - 1 and sp_activated:
            sp_meter = 0
            sp_activated = False
        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, curr_score)
    
    return max_score

