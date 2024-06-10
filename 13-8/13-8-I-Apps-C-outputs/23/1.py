
def get_max_score(notes, sp_phrases):
    
    # Initialize the score and SP meter
    score = 0
    sp_meter = 0

    # Iterate through the notes and Star Power phrases
    for i in range(len(notes)):
        # Check if the current note is within a Star Power phrase
        for j in range(len(sp_phrases)):
            if notes[i] >= sp_phrases[j][0] and notes[i] <= sp_phrases[j][1]:
                # Add the score for the current note
                score += 1

                # Check if the current note is the first or last note of a Star Power phrase
                if notes[i] == sp_phrases[j][0] or notes[i] == sp_phrases[j][1]:
                    # Add the score for the current note
                    score += 1

                # Add the SP meter for the current note
                sp_meter += 1

                # Break out of the inner loop
                break

    # Return the maximum score
    return score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = []
    for i in range(p):
        sp_phrases.append(list(map(int, input().split())))

    # Find the maximum score
    score = get_max_score(notes, sp_phrases)

    # Print the maximum score
    print(score)

if __name__ == '__main__':
    main()

