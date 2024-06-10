
def get_maximum_score(notes, sp_phrases):
    # Initialize variables
    score = 0
    sp_meter = 0
    sp_activated = False

    # Sort the notes and SP phrases by position
    notes.sort()
    sp_phrases.sort(key=lambda x: x[0])

    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for j in range(len(sp_phrases)):
            if notes[i] >= sp_phrases[j][0] and notes[i] <= sp_phrases[j][1]:
                # Check if the SP meter is positive and the note is the first or last note of the SP phrase
                if sp_meter > 0 and (notes[i] == sp_phrases[j][0] or notes[i] == sp_phrases[j][1]):
                    # Activate Star Power and update the SP meter
                    sp_activated = True
                    sp_meter = 0
                    break
                # Update the SP meter
                sp_meter += 1
                break
        # Add the score for the current note
        if sp_activated:
            score += 2
        else:
            score += 1
        # Reset the SP activated flag
        sp_activated = False

    return score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [list(map(int, input().split())) for _ in range(p)]

    # Get the maximum score
    score = get_maximum_score(notes, sp_phrases)

    # Print the result
    print(score)

if __name__ == '__main__':
    main()

