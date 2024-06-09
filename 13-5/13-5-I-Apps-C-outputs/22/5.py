
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Initialize the SP meter and the current SP charge
    sp_meter = 0
    current_sp_charge = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # If the current note is within an SP phrase, charge up the SP meter
        if i in sp_phrases:
            sp_meter += 1
        
        # If the current note is the first note of an SP phrase, activate Star Power
        if i == sp_phrases[0]:
            current_sp_charge = sp_meter
            sp_meter = 0
        
        # If the current note is the last note of an SP phrase, drain the SP meter
        if i == sp_phrases[-1]:
            sp_meter += current_sp_charge
            current_sp_charge = 0
        
        # Add the score for the current note
        current_score += 1
        
        # If Star Power is activated, add the score for the current note
        if sp_meter > 0:
            current_score += 1
        
        # Update the maximum score
        max_score = max(max_score, current_score)
    
    return max_score

