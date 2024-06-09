
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for j in range(len(sp_phrases)):
            if notes[i] >= sp_phrases[j][0] and notes[i] <= sp_phrases[j][1]:
                # If it is, add the score for the SP phrase
                current_score += sp_phrases[j][1] - sp_phrases[j][0] + 1
                break
        # Add the score for the current note
        current_score += 1
        
        # Update the maximum score if necessary
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = []
    for i in range(p):
        s, e = map(int, input().split())
        sp_phrases.append([s, e])
    
    # Call the function to get the maximum score
    max_score = get_max_score(notes, sp_phrases)
    
    # Print the result
    print(max_score)

if __name__ == '__main__':
    main()

