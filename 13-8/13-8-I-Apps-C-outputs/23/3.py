
def get_max_score(notes, sp_phrases):
    # Initialize the max score and SP meter
    max_score = 0
    sp_meter = 0

    # Iterate through the notes and SP phrases
    for i, note in enumerate(notes):
        # Check if the note is within an SP phrase
        for sp in sp_phrases:
            if sp[0] <= note <= sp[1]:
                # If the note is within an SP phrase, charge up the SP meter
                sp_meter += 1
                break

        # If the note is not within an SP phrase, score it normally
        if sp_meter == 0:
            max_score += 1

        # If the note is the last note of an SP phrase, drain the SP meter
        if i == sp[1]:
            sp_meter = 0

    return max_score

def main():
    # Read the input
    n, p = map(int, input().split())
    notes = list(map(int, input().split()))
    sp_phrases = [list(map(int, input().split())) for _ in range(p)]

    # Get the maximum score
    max_score = get_max_score(notes, sp_phrases)

    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

