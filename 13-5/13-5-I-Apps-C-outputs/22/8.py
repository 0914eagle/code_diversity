
def get_max_score(notes, sp_phrases):
    # Initialize variables
    max_score = 0
    sp_meter = 0
    sp_activated = False

    # Iterate through the notes
    for i in range(len(notes)):
        # Check if the note is within an SP phrase
        for sp in sp_phrases:
            if notes[i] >= sp[0] and notes[i] <= sp[1]:
                # If the note is within an SP phrase, charge up the SP meter
                sp_meter += 1
                break

        # If the SP meter is positive, activate Star Power
        if sp_meter > 0:
            sp_activated = True
            max_score += 2

        # If the note is the last note of an SP phrase, drain the SP meter
        if sp_activated and i == len(notes) - 1:
            sp_meter = 0
            sp_activated = False

    return max_score

def main():
    # Read input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = []
    for i in range(p):
        sp_phrases.append(list(map(int, input().split())))

    # Get the maximum score
    max_score = get_max_score(notes, sp_phrases)

    # Print output
    print(max_score)

if __name__ == '__main__':
    main()

