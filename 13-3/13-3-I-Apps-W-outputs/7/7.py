
def get_maximum_height(notes):
    # Sort the notes by day
    notes.sort(key=lambda x: x[0])
    # Initialize the maximum height and the current height
    max_height = 0
    current_height = 0
    # Iterate through the notes
    for day, height in notes:
        # Check if the height is consistent with the current height
        if abs(height - current_height) <= 1:
            # Update the current height and the maximum height
            current_height = height
            max_height = max(max_height, height)
        else:
            # The height is not consistent, return 'IMPOSSIBLE'
            return 'IMPOSSIBLE'
    # Return the maximum height
    return max_height

def main():
    # Read the number of days and notes
    n, m = map(int, input().split())
    # Read the notes
    notes = []
    for _ in range(m):
        day, height = map(int, input().split())
        notes.append((day, height))
    # Get the maximum height
    max_height = get_maximum_height(notes)
    # Print the result
    print(max_height)

if __name__ == '__main__':
    main()

