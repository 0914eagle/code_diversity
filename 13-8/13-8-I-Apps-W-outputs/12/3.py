
def get_max_notes(a, b):
    # Initialize variables
    max_notes = 0
    notes_first_day = []
    notes_second_day = []
    
    # Iterate through all possible combinations of notes
    for i in range(1, a+1):
        for j in range(1, b+1):
            # Check if the sum of hours is less than or equal to the total hours
            if i + j <= a + b:
                # Check if the number of notes is greater than the current maximum
                if i + j > max_notes:
                    # Update the maximum number of notes
                    max_notes = i + j
                    # Update the notes for the first day
                    notes_first_day = [k for k in range(1, i+1)]
                    # Update the notes for the second day
                    notes_second_day = [k for k in range(i+1, i+j+1)]
    
    # Return the maximum number of notes and the notes for the first and second day
    return max_notes, notes_first_day, notes_second_day

def main():
    # Read the input
    a, b = map(int, input().split())
    
    # Get the maximum number of notes and the notes for the first and second day
    max_notes, notes_first_day, notes_second_day = get_max_notes(a, b)
    
    # Print the output
    print(len(notes_first_day))
    print(*notes_first_day)
    print(len(notes_second_day))
    print(*notes_second_day)

if __name__ == '__main__':
    main()

