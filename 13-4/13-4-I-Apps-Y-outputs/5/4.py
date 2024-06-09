
def get_handshakes(seating_order):
    # Initialize variables
    handshakes = 0
    rows, cols = len(seating_order), len(seating_order[0])

    # Loop through each row and column
    for i in range(rows):
        for j in range(cols):
            # Check if the current element is a person
            if seating_order[i][j] == "o":
                # Check if there are any empty seats in the current row
                if "." in seating_order[i]:
                    # Count the number of handshakes in the current row
                    handshakes += seating_order[i].count("o") - 1
                # Check if there are any empty seats in the current column
                if "." in [row[j] for row in seating_order]:
                    # Count the number of handshakes in the current column
                    handshakes += sum(1 for row in seating_order if row[j] == "o") - 1
                # Check if there are any empty seats in the current diagonal
                if i + j < rows and "." in [seating_order[k][k] for k in range(i, rows)]:
                    # Count the number of handshakes in the current diagonal
                    handshakes += sum(1 for k in range(i, rows) if seating_order[k][k] == "o") - 1
                # Check if there are any empty seats in the current anti-diagonal
                if i - j >= 0 and "." in [seating_order[k][rows - k - 1] for k in range(i + 1)]:
                    # Count the number of handshakes in the current anti-diagonal
                    handshakes += sum(1 for k in range(i + 1) if seating_order[k][rows - k - 1] == "o") - 1

    return handshakes

def main():
    # Read the input
    rows, cols = map(int, input().split())
    seating_order = [input() for _ in range(rows)]

    # Calculate the handshakes
    handshakes = get_handshakes(seating_order)

    # Print the result
    print(handshakes)

if __name__ == '__main__':
    main()

