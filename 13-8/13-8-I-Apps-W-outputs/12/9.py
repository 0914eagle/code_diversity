
def get_notes_to_read(a, b):
    # Initialize a list to store the notes to read
    notes_to_read = []
    
    # Iterate from 1 to a
    for i in range(1, a + 1):
        # If i is divisible by a, add it to the list of notes to read
        if i % a == 0:
            notes_to_read.append(i)
    
    # Return the list of notes to read
    return notes_to_read

def get_notes_to_read_in_days(a, b):
    # Get the list of notes to read in the first day
    notes_to_read_1 = get_notes_to_read(a, 0)
    
    # Get the list of notes to read in the second day
    notes_to_read_2 = get_notes_to_read(0, b)
    
    # Return the list of notes to read in the first day and the list of notes to read in the second day
    return notes_to_read_1, notes_to_read_2

if __name__ == '__main__':
    a, b = map(int, input().split())
    notes_to_read_1, notes_to_read_2 = get_notes_to_read_in_days(a, b)
    print(len(notes_to_read_1))
    print(*notes_to_read_1)
    print(len(notes_to_read_2))
    print(*notes_to_read_2)

