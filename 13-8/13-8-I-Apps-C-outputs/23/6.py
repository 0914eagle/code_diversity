
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Initialize the SP meter and the SP charge
    sp_meter = 0
    sp_charge = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # If the current note is within an SP phrase, charge up the SP meter
        if i in sp_phrases:
            sp_meter += 1
        
        # If the SP meter is positive, activate Star Power and double the score
        if sp_meter > 0:
            current_score *= 2
        
        # If the current note is the last note of an SP phrase, drain the SP meter
        if i == sp_phrases[-1]:
            sp_meter = 0
        
        # Add the current score to the maximum score
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = []
    for i in range(p):
        s, e = map(int, input().split())
        sp_phrases.append(s)
        sp_phrases.append(e)
    
    # Get the maximum score
    max_score = get_max_score(notes, sp_phrases)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

