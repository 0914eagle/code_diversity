
def get_maximum_height(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Initialize the maximum height and the current height
    max_height = 0
    current_height = 0
    # Iterate through the notes
    for note in notes:
        # Check if the current height is consistent with the previous note
        if current_height - note[1] <= 1:
            # Update the current height
            current_height = note[1]
            # Update the maximum height
            max_height = max(max_height, current_height)
        else:
            # The notes are inconsistent, return 'IMPOSSIBLE'
            return 'IMPOSSIBLE'
    # Return the maximum height
    return max_height

def main():
    # Read the number of days and notes
    n, m = map(int, input().split())
    # Read the notes
    notes = []
    for i in range(m):
        d, h = map(int, input().split())
        notes.append((d, h))
    # Get the maximum height
    max_height = get_maximum_height(notes)
    # Print the result
    print(max_height)

if __name__ == '__main__':
    main()

