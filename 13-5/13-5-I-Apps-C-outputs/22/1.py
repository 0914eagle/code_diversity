
def get_max_score(notes, sp_phrases):
    
    # Initialize the maximum score and the current score
    max_score = 0
    current_score = 0

    # Iterate through the notes and Star Power phrases
    for i, note in enumerate(notes):
        # Check if the current note is within a Star Power phrase
        for sp_phrase in sp_phrases:
            if sp_phrase[0] <= note <= sp_phrase[1]:
                # If the note is within a Star Power phrase, charge up the SP meter
                current_score += 2
                break
        else:
            # If the note is not within a Star Power phrase, score a regular note
            current_score += 1

        # If the current score is greater than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score

    return max_score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [tuple(map(int, input().split())) for _ in range(p)]

    # Find the maximum score
    max_score = get_max_score(notes, sp_phrases)

    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

