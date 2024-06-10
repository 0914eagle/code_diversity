
def get_max_score(notes, sp_phrases):
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # If the current note is within an SP phrase, charge up the SP meter
        if i in sp_phrases:
            current_score += 1
        # If the current note is not within an SP phrase, deduct one point from the current score
        else:
            current_score -= 1
        
        # Update the maximum score if the current score is higher
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

def main():
    # Read the input data
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]
    
    # Find the maximum score
    max_score = get_max_score(notes, sp_phrases)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

