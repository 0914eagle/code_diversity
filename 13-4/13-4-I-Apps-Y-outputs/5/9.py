
def get_handshakes(seating_order):
    # Initialize variables
    handshakes = 0
    rows, cols = len(seating_order), len(seating_order[0])

    # Iterate through the seating order
    for i in range(rows):
        for j in range(cols):
            # Check if the current element is a person
            if seating_order[i][j] == "o":
                # Increment the handshakes count
                handshakes += 1
                # Check if the current element has neighbors
                if i > 0 and j > 0 and seating_order[i-1][j-1] == "o":
                    handshakes += 1
                if i > 0 and seating_order[i-1][j] == "o":
                    handshakes += 1
                if i > 0 and j < cols-1 and seating_order[i-1][j+1] == "o":
                    handshakes += 1
                if j > 0 and seating_order[i][j-1] == "o":
                    handshakes += 1
                if j < cols-1 and seating_order[i][j+1] == "o":
                    handshakes += 1
                if i < rows-1 and j > 0 and seating_order[i+1][j-1] == "o":
                    handshakes += 1
                if i < rows-1 and seating_order[i+1][j] == "o":
                    handshakes += 1
                if i < rows-1 and j < cols-1 and seating_order[i+1][j+1] == "o":
                    handshakes += 1

    return handshakes

def main():
    # Read the seating order from stdin
    rows, cols = map(int, input().split())
    seating_order = []
    for _ in range(rows):
        seating_order.append(input())

    # Calculate the handshakes
    handshakes = get_handshakes(seating_order)

    # Print the result
    print(handshakes)

if __name__ == '__main__':
    main()

