
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
        if sp_phrases and notes[i] in range(sp_phrases[0][0], sp_phrases[0][1]):
            # If the SP meter is positive, activate Star Power
            if sp_meter > 0:
                sp_activated = True
                current_score += 2
            # Add the note to the current score
            current_score += 1
            # Decrement the SP meter
            sp_meter -= 1
        # If the current note is not within an SP phrase, add it to the current score
        else:
            current_score += 1
    
    # If Star Power is activated, add the current score to the maximum score
    if sp_activated:
        max_score += current_score
    
    # Return the maximum score
    return max_score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [list(map(int, input().split())) for _ in range(p)]
    
    # Get the maximum score
    max_score = get_max_score(notes, sp_phrases)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

