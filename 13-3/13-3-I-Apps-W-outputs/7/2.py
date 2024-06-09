
def get_maximum_height(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Initialize the maximum height and the current height
    max_height = 0
    current_height = 0
    # Iterate through the notes
    for note in notes:
        # If the current height is less than the note height, set the current height to the note height
        if current_height < note[1]:
            current_height = note[1]
        # If the current height is greater than the max height, set the max height to the current height
        if current_height > max_height:
            max_height = current_height
    return max_height

def is_consistent(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Iterate through the notes
    for i in range(len(notes) - 1):
        # If the difference between the current day and the next day is greater than 1, return False
        if notes[i+1][0] - notes[i][0] > 1:
            return False
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

