
def get_maximum_height(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Initialize the maximum height and the current height
    max_height = 0
    current_height = 0
    # Iterate through the notes
    for note in notes:
        # If the current height is less than the height in the note, set the current height to the height in the note
        if current_height < note[1]:
            current_height = note[1]
        # If the current height is greater than the maximum height, set the maximum height to the current height
        if current_height > max_height:
            max_height = current_height
    return max_height

def main():
    n, m = map(int, input().split())
    notes = []
    for i in range(m):
        d, h = map(int, input().split())
        notes.append((d, h))
    print(get_maximum_height(notes))

if __name__ == '__main__':
    main()

