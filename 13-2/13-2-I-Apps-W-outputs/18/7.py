
a, b = map(int, input().split())

# Find the maximum number of notes that can be read in a day
max_notes = min(a, b)

# Initialize the list of notes to read in the first day
notes_first_day = []

# Initialize the list of notes to read in the second day
notes_second_day = []

# Loop through the maximum number of notes that can be read in a day
for i in range(1, max_notes + 1):
    # Check if the current note can be read in the first day
    if i <= a:
        # Add the current note to the list of notes to read in the first day
        notes_first_day.append(i)
    
    # Check if the current note can be read in the second day
    if i <= b:
        # Add the current note to the list of notes to read in the second day
        notes_second_day.append(i)

# Print the number of notes to read in the first day
print(len(notes_first_day))

# Print the notes to read in the first day
print(*notes_first_day)

# Print the number of notes to read in the second day
print(len(notes_second_day))

# Print the notes to read in the second day
print(*notes_second_day)

