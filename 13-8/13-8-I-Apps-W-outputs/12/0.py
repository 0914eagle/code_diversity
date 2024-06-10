
def read_notes(a, b):
    # Find the maximum number of notes that can be read in a day
    max_notes = a if a < b else b

    # Initialize the list of notes to read in the first day
    notes_today = []

    # Initialize the list of notes to read in the second day
    notes_tomorrow = []

    # Loop through the range of notes
    for i in range(1, max_notes + 1):
        # Check if the current note can be read in the first day
        if i <= a:
            # Add the note to the list of notes to read in the first day
            notes_today.append(i)

        # Check if the current note can be read in the second day
        if i <= b:
            # Add the note to the list of notes to read in the second day
            notes_tomorrow.append(i)

    # Return the lists of notes to read in the first and second days
    return notes_today, notes_tomorrow

def main():
    # Read the number of hours Lesha has today and tomorrow
    a, b = map(int, input().split())

    # Call the read_notes function to get the lists of notes to read in the first and second days
    notes_today, notes_tomorrow = read_notes(a, b)

    # Print the number of notes to read in the first day
    print(len(notes_today))

    # Print the list of notes to read in the first day
    print(*notes_today)

    # Print the number of notes to read in the second day
    print(len(notes_tomorrow))

    # Print the list of notes to read in the second day
    print(*notes_tomorrow)

if __name__ == '__main__':
    main()

