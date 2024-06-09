
def get_handshakes(seating_order):
    # Initialize variables
    handshakes = 0
    rows, cols = len(seating_order), len(seating_order[0])

    # Loop through each row and column
    for i in range(rows):
        for j in range(cols):
            # Check if the current element is a person
            if seating_order[i][j] == "o":
                # Check if there are any neighbors in the current row
                if j > 0 and seating_order[i][j-1] == "o":
                    handshakes += 1
                if j < cols-1 and seating_order[i][j+1] == "o":
                    handshakes += 1
                # Check if there are any neighbors in the current column
                if i > 0 and seating_order[i-1][j] == "o":
                    handshakes += 1
                if i < rows-1 and seating_order[i+1][j] == "o":
                    handshakes += 1

    return handshakes

def main():
    # Read input
    rows, cols = map(int, input().split())
    seating_order = [input() for _ in range(rows)]

    # Calculate handshakes
    handshakes = get_handshakes(seating_order)

    # Print output
    print(handshakes)

if __name__ == '__main__':
    main()

