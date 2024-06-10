
def get_notes(a, b):
    # Initialize variables
    notes = []
    hours = 0
    
    # Iterate through the possible notes
    for i in range(1, a+1):
        # Check if the current note can be read in the remaining time
        if hours + i <= a:
            # Add the note to the list of notes to read
            notes.append(i)
            # Update the number of hours spent
            hours += i
    
    # Return the list of notes to read
    return notes

def get_notes_per_day(notes, a, b):
    # Initialize variables
    notes_per_day = []
    hours = 0
    
    # Iterate through the notes
    for i in range(len(notes)):
        # Check if the current note can be read in the remaining time
        if hours + notes[i] <= a:
            # Add the note to the list of notes to read in the first day
            notes_per_day.append(notes[i])
            # Update the number of hours spent
            hours += notes[i]
        else:
            # Add the note to the list of notes to read in the second day
            notes_per_day.append(notes[i])
            # Update the number of hours spent
            hours += notes[i]
    
    # Return the list of notes to read in each day
    return notes_per_day

def main():
    # Read the input
    a, b = map(int, input().split())
    
    # Get the list of notes to read
    notes = get_notes(a, b)
    
    # Get the list of notes to read in each day
    notes_per_day = get_notes_per_day(notes, a, b)
    
    # Print the output
    print(len(notes_per_day[0]))
    print(*notes_per_day[0])
    print(len(notes_per_day[1]))
    print(*notes_per_day[1])

if __name__ == '__main__':
    main()

