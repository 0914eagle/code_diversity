
def get_maximum_height(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Initialize the maximum height and the current height
    max_height = 0
    current_height = 0
    # Iterate through the notes
    for note in notes:
        # If the current height is less than the height in the note, update the current height and maximum height
        if current_height < note[1]:
            current_height = note[1]
            max_height = max(max_height, current_height)
        # If the current height is greater than the height in the note, update the current height
        elif current_height > note[1]:
            current_height = note[1]
    # Return the maximum height
    return max_height

def is_consistent(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Iterate through the notes
    for i in range(len(notes) - 1):
        # If the difference between the heights on consecutive days is greater than 1, return False
        if abs(notes[i][1] - notes[i+1][1]) > 1:
            return False
    # If all the differences are less than or equal to 1, return True
    return True

def main():
    n, m = map(int, input().split())
    notes = []
    for i in range(m):
        d, h = map(int, input().split())
        notes.append((d, h))
    if is_consistent(notes):
        print(get_maximum_height(notes))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()

