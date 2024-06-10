
def get_maximum_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Initialize the SP meter and the SP activation flag
    sp_meter = 0
    sp_activated = False
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for j in range(len(sp_phrases)):
            if notes[i] >= sp_phrases[j][0] and notes[i] <= sp_phrases[j][1]:
                # If the SP meter is positive, activate Star Power
                if sp_meter > 0:
                    sp_activated = True
                    break
        
        # If Star Power is activated, add two points to the current score
        if sp_activated:
            current_score += 2
        
        # If the current note is the first or last note of an SP phrase, add one point to the current score
        if notes[i] == sp_phrases[j][0] or notes[i] == sp_phrases[j][1]:
            current_score += 1
        
        # Update the SP meter and the SP activation flag
        if sp_activated:
            sp_meter -= 1
            if sp_meter == 0:
                sp_activated = False
        
        # Update the maximum score
        max_score = max(max_score, current_score)
    
    return max_score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [list(map(int, input().split())) for _ in range(p)]
    
    # Find the maximum score
    max_score = get_maximum_score(notes, sp_phrases)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

