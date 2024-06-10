
def get_notes_and_sp_phrases(notes_file, sp_phrases_file):
    with open(notes_file, "r") as f:
        notes = [int(note) for note in f.readline().split()]
    with open(sp_phrases_file, "r") as f:
        sp_phrases = [(int(start), int(end)) for start, end in [line.split() for line in f.readlines()]]
    return notes, sp_phrases

def get_max_score(notes, sp_phrases):
    # Initialize variables
    score = 0
    sp_meter = 0
    sp_activated = False
    sp_phrase_idx = 0

    # Iterate through the notes
    for i, note in enumerate(notes):
        # Check if the note is within an SP phrase
        if sp_phrase_idx < len(sp_phrases) and note >= sp_phrases[sp_phrase_idx][0] and note <= sp_phrases[sp_phrase_idx][1]:
            # Activate SP if necessary
            if not sp_activated:
                sp_activated = True
                sp_meter = 1
            # Increase SP meter
            sp_meter += 1
            # Check if the note is the last note of an SP phrase
            if note == sp_phrases[sp_phrase_idx][1]:
                sp_phrase_idx += 1
                sp_activated = False
        # Check if SP is activated and the note is not within an SP phrase
        elif sp_activated and note not in range(sp_phrases[sp_phrase_idx][0], sp_phrases[sp_phrase_idx][1]):
            # Drain SP meter
            sp_meter -= 1
            # Check if SP meter is empty
            if sp_meter == 0:
                sp_activated = False
        # Add score for the note
        if sp_activated and note not in range(sp_phrases[sp_phrase_idx][0], sp_phrases[sp_phrase_idx][1]):
            score += 2
        else:
            score += 1

    return score

def main():
    notes_file = "notes.txt"
    sp_phrases_file = "sp_phrases.txt"
    notes, sp_phrases = get_notes_and_sp_phrases(notes_file, sp_phrases_file)
    print(get_max_score(notes, sp_phrases))

if __name__ == '__main__':
    main()

