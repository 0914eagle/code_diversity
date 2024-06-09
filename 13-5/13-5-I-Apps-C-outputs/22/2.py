
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Initialize the SP meter and the SP activation flag
    sp_meter = 0
    sp_activated = False
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        if any(notes[i] in range(sp_phrases[j][0], sp_phrases[j][1]) for j in range(len(sp_phrases))):
            # If the SP meter is not activated, activate it and add the SP bonus
            if not sp_activated:
                sp_activated = True
                current_score += 2
            
            # Add the SP bonus for the current note
            current_score += 2
        
        # If the current note is not within an SP phrase, add the regular note score
        else:
            current_score += 1
        
        # If the current note is the last note of an SP phrase, deactivate the SP meter
        if sp_activated and i == sp_phrases[-1][1] - 1:
            sp_activated = False
        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

def main():
    # Read the input notes and SP phrases
    notes = [int(x) for x in input().split()]
    sp_phrases = [[int(x) for x in input().split()] for _ in range(int(input()))]
    
    # Get the maximum score
    max_score = get_max_score(notes, sp_phrases)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

