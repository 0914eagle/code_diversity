
def get_handshakes(seating_order):
    # Initialize variables
    handshakes = 0
    rows, cols = len(seating_order), len(seating_order[0])

    # Iterate through the seating order
    for i in range(rows):
        for j in range(cols):
            # Check if the current element is a person
            if seating_order[i][j] == "o":
                # Check if there are any empty seats in the current row
                if j < cols - 1 and seating_order[i][j + 1] == ".":
                    handshakes += 1
                # Check if there are any empty seats in the current column
                if i < rows - 1 and seating_order[i + 1][j] == ".":
                    handshakes += 1
                # Check if there are any empty seats in the current diagonal
                if i < rows - 1 and j < cols - 1 and seating_order[i + 1][j + 1] == ".":
                    handshakes += 1
                # Check if there are any empty seats in the current anti-diagonal
                if i < rows - 1 and j > 0 and seating_order[i + 1][j - 1] == ".":
                    handshakes += 1

    return handshakes

def main():
    rows, cols = map(int, input().split())
    seating_order = [input() for _ in range(rows)]
    print(get_handshakes(seating_order))

if __name__ == '__main__':
    main()

