
def max_notes(a, b):
    # Find the maximum number of notes that can be read in a day
    max_notes_per_day = a if a > b else b

    # Initialize the number of notes read in the first day to 0
    num_notes_first_day = 0

    # Initialize the number of notes read in the second day to 0
    num_notes_second_day = 0

    # Initialize the current hour to 0
    current_hour = 0

    # Initialize the list of notes read in the first day
    notes_first_day = []

    # Initialize the list of notes read in the second day
    notes_second_day = []

    # Iterate until the maximum number of notes per day is reached
    while num_notes_first_day < max_notes_per_day and num_notes_second_day < max_notes_per_day:
        # If the current hour is odd, read a note in the first day
        if current_hour % 2 == 1:
            num_notes_first_day += 1
            notes_first_day.append(current_hour)

        # If the current hour is even, read a note in the second day
        else:
            num_notes_second_day += 1
            notes_second_day.append(current_hour)

        # Increment the current hour
        current_hour += 1

    # Return the maximum number of notes read in total
    return num_notes_first_day + num_notes_second_day

def main():
    a, b = map(int, input().split())
    max_notes = max_notes(a, b)
    print(max_notes)

if __name__ == '__main__':
    main()

