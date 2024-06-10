
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    curr_score = 0
    
    # Initialize the SP meter and the timer
    sp_meter = 0
    timer = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # If the current note is within an SP phrase, charge up the SP meter
        if any(notes[i] in range(sp_phrase[0], sp_phrase[1]) for sp_phrase in sp_phrases):
            sp_meter += 1
        
        # If the current note is the first or last note of an SP phrase, activate Star Power
        if notes[i] in (sp_phrase[0], sp_phrase[1] - 1) for sp_phrase in sp_phrases:
            timer += sp_meter
            sp_meter = 0
        
        # If Star Power is activated, give a score of 2 for the current note
        if timer > 0:
            curr_score += 2
        else:
            curr_score += 1
        
        # Update the maximum score
        max_score = max(max_score, curr_score)
    
    return max_score

