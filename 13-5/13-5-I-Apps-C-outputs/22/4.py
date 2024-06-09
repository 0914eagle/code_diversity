
def get_max_score(notes, sp_phrases):
    
    # Initialize variables
    score = 0
    sp_meter = 0
    sp_activated = False

    # Iterate through the notes and SP phrases
    for i in range(len(notes)):
        # Check if the current note is within an SP phrase
        for sp_phrase in sp_phrases:
            if notes[i] in range(sp_phrase[0], sp_phrase[1]):
                # If the SP meter is not activated, activate it and add the SP phrase to the score
                if not sp_activated:
                    sp_meter += sp_phrase[1] - sp_phrase[0]
                    score += sp_phrase[1] - sp_phrase[0]
                    sp_activated = True
                # If the SP meter is already activated, check if the current note is the first or last note of the SP phrase
                else:
                    if notes[i] == sp_phrase[0] or notes[i] == sp_phrase[1] - 1:
                        score += 1
                    else:
                        score += 2

        # If the current note is not within an SP phrase, add it to the score
        if not sp_activated:
            score += 1

        # Decrement the SP meter by 1 if it is activated
        if sp_activated:
            sp_meter -= 1
            if sp_meter == 0:
                sp_activated = False

    return score

def main():
    # Read input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [list(map(int, input().split())) for _ in range(p)]

    # Calculate maximum score
    score = get_max_score(notes, sp_phrases)

    # Print output
    print(score)

if __name__ == '__main__':
    main()

