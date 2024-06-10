
def read_notes(a, b):
    # Find the maximum number of notes that can be read in a and b hours
    max_notes = min(a, b)

    # Initialize the list of notes to read in the first day
    first_day = []

    # Initialize the list of notes to read in the second day
    second_day = []

    # Iterate from 1 to max_notes
    for i in range(1, max_notes + 1):
        # If i hours is enough to read the current note
        if i <= a:
            # Add the current note to the first day
            first_day.append(i)
        # If i hours is not enough to read the current note
        else:
            # Add the current note to the second day
            second_day.append(i)

    # Return the lists of notes to read in the first and second days
    return first_day, second_day

def main():
    # Read the number of hours Lesha has today and tomorrow
    a, b = map(int, input().split())

    # Call the read_notes function to get the lists of notes to read in the first and second days
    first_day, second_day = read_notes(a, b)

    # Print the number of notes Lesha has to read in the first day
    print(len(first_day))

    # Print the notes Lesha has to read in the first day
    for note in first_day:
        print(note, end=" ")

    # Print the number of notes Lesha has to read in the second day
    print()
    print(len(second_day))

    # Print the notes Lesha has to read in the second day
    for note in second_day:
        print(note, end=" ")

if __name__ == '__main__':
    main()

