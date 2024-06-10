
def get_notes(notes):
    # Split the notes into individual notes
    notes = notes.split()
    
    # Initialize an empty list to store the notes
    staff_notes = []
    
    # Iterate through the notes
    for note in notes:
        # Check if the note has a duration
        if len(note) == 1:
            # Add the note to the staff with a default duration of 1
            staff_notes.append(note)
        else:
            # Add the note to the staff with the specified duration
            staff_notes.append(note[0] * int(note[1]))
    
    return staff_notes

def create_staff(notes):
    # Initialize an empty list to store the staff
    staff = []
    
    # Iterate through the notes
    for note in notes:
        # Check if the note is a rest
        if note == "R":
            # Add a rest to the staff
            staff.append(" ")
        else:
            # Add the note to the staff
            staff.append(note)
    
    return staff

def print_staff(staff):
    # Print the staff
    print("\n".join(staff))

if __name__ == '__main__':
    # Get the input notes
    notes = input("Enter the notes: ")
    
    # Get the staff notes
    staff_notes = get_notes(notes)
    
    # Create the staff
    staff = create_staff(staff_notes)
    
    # Print the staff
    print_staff(staff)

