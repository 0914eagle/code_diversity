
def get_sequence_of_moves(grid):
    # Initialize the sequence of moves
    sequence = []
    
    # Loop through each row of the grid
    for row in grid:
        # Loop through each cell in the row
        for i in range(len(row)):
            # Check if the current cell is empty
            if row[i] == "E":
                # Check if the cell to the left is an organ
                if i > 0 and row[i-1] != "E":
                    # Add a move to the left to the sequence
                    sequence.append("l")
                # Check if the cell to the right is an organ
                elif i < len(row)-1 and row[i+1] != "E":
                    # Add a move to the right to the sequence
                    sequence.append("r")
                # Check if the cell is in the top row
                elif row == grid[0]:
                    # Add a move up to the sequence
                    sequence.append("u")
                # Check if the cell is in the bottom row
                elif row == grid[-1]:
                    # Add a move down to the sequence
                    sequence.append("d")
    
    # Return the sequence of moves
    return "".join(sequence)

def get_shortcuts(sequence):
    # Initialize the shortcuts
    shortcuts = {}
    
    # Loop through each character in the sequence
    for i in range(len(sequence)):
        # Check if the current character is a move
        if sequence[i] in ["u", "d", "l", "r"]:
            # Check if the current character is the start of a shortcut
            if i+1 < len(sequence) and sequence[i+1] == sequence[i]:
                # Initialize the shortcut
                shortcut = sequence[i]
                # Loop through each subsequent character in the sequence
                for j in range(i+2, len(sequence)):
                    # Check if the current character is the end of the shortcut
                    if sequence[j] != sequence[i]:
                        # Add the shortcut to the dictionary
                        shortcuts[shortcut] = sequence[i:j]
                        # Break out of the loop
                        break
    
    # Return the shortcuts
    return shortcuts

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        # Read the size of the grid
        k = int(input())
        # Read the grid
        grid = [input() for _ in range(2*k+1)]
        # Get the sequence of moves
        sequence = get_sequence_of_moves(grid)
        # Get the shortcuts
        shortcuts = get_shortcuts(sequence)
        # Print the shortcuts
        for shortcut in shortcuts:
            print(shortcut, shortcuts[shortcut])
        # Print the final sequence of moves
        print("DONE")

if __name__ == '__main__':
    main()

