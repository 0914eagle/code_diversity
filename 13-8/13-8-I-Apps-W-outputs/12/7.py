
def read_notes_in_first_day(hours_available, notes_count):
    # Initialize a list to store the notes to be read in the first day
    notes_to_read = []
    
    # Iterate through the notes from 1 to notes_count
    for i in range(1, notes_count + 1):
        # If the current note can be read in the available hours, add it to the list of notes to read in the first day
        if i <= hours_available:
            notes_to_read.append(i)
    
    # Return the list of notes to read in the first day
    return notes_to_read

def read_notes_in_second_day(hours_available, notes_count, notes_read_in_first_day):
    # Initialize a list to store the notes to be read in the second day
    notes_to_read = []
    
    # Iterate through the notes from 1 to notes_count
    for i in range(1, notes_count + 1):
        # If the current note is not in the list of notes read in the first day and can be read in the available hours, add it to the list of notes to read in the second day
        if i not in notes_read_in_first_day and i <= hours_available:
            notes_to_read.append(i)
    
    # Return the list of notes to read in the second day
    return notes_to_read

def main():
    # Read the input data
    hours_available_first_day, hours_available_second_day = map(int, input().split())
    
    # Calculate the total number of hours available
    total_hours_available = hours_available_first_day + hours_available_second_day
    
    # Calculate the number of notes that can be read in the first day
    notes_to_read_first_day = read_notes_in_first_day(hours_available_first_day, total_hours_available)
    
    # Calculate the number of notes that can be read in the second day
    notes_to_read_second_day = read_notes_in_second_day(hours_available_second_day, total_hours_available, notes_to_read_first_day)
    
    # Print the output
    print(len(notes_to_read_first_day))
    print(*notes_to_read_first_day)
    print(len(notes_to_read_second_day))
    print(*notes_to_read_second_day)

if __name__ == '__main__':
    main()

