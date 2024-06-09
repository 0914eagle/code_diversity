
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Initialize the SP meter and the SP activation flag
    sp_meter = 0
    sp_activated = False
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # If the current note is within an SP phrase, activate the SP meter
        if sp_activated:
            sp_meter += 1
        
        # If the current note is the start of an SP phrase, activate the SP meter
        if i in sp_phrases:
            sp_activated = True
            sp_meter = 1
        
        # If the current note is the end of an SP phrase, deactivate the SP meter
        if i == sp_phrases[-1]:
            sp_activated = False
            sp_meter = 0
        
        # If the SP meter is positive and the current note is the start of an SP phrase, do not count the note
        if sp_meter > 0 and i in sp_phrases:
            continue
        
        # If the SP meter is positive and the current note is the end of an SP phrase, count the note as worth one point
        if sp_meter > 0 and i == sp_phrases[-1]:
            current_score += 1
        
        # If the SP meter is not positive, count the note as worth two points
        else:
            current_score += 2
        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

