
def get_max_squares(n, a):
    # Initialize variables
    max_squares = 0
    current_color = 1
    remaining_liters = a.copy()

    # Loop through each color
    for i in range(n):
        # Calculate the number of squares that can be painted with the current color
        num_squares = min(remaining_liters[i], (n - i) // (i + 1))

        # Update the maximum number of squares
        max_squares = max(max_squares, num_squares)

        # Update the current color and the remaining liters
        current_color = (current_color + 1) % (i + 1)
        remaining_liters[current_color] -= num_squares

    return max_squares

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_squares(n, a))

if __name__ == '__main__':
    main()

