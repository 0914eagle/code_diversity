
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # If the current note is within an SP phrase, activate Star Power
        if i in sp_phrases:
            current_score *= 2
        
        # Add the score for the current note to the current score
        current_score += 1
        
        # Update the maximum score if the current score is higher
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
        sp_phrases.append(range(s, e + 1))
    
    # Get the maximum score
    max_score = get_max_score(notes, sp_phrases)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

