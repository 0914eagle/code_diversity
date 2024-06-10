
def get_max_score(notes, sp_phrases):
    # Initialize variables
    max_score = 0
    sp_meter = 0
    sp_activated = False

    # Iterate through the notes
    for i in range(len(notes)):
        # Check if the note is part of an SP phrase
        if sp_activated:
            # If the SP meter is positive, the note is worth 2 points
            if sp_meter > 0:
                max_score += 2
            # If the SP meter is negative, the note is worth 1 point
            else:
                max_score += 1
            # Decrement the SP meter
            sp_meter -= 1
        # If the note is not part of an SP phrase, it is worth 1 point
        else:
            max_score += 1
        # Check if the note is the start of an SP phrase
        if notes[i] in sp_phrases:
            # Set the SP meter to the maximum value
            sp_meter = 50000000
            # Set the SP activated flag to True
            sp_activated = True

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

    # Call the function to get the maximum score
    max_score = get_max_score(notes, sp_phrases)

    # Print the result
    print(max_score)

if __name__ == '__main__':
    main()

