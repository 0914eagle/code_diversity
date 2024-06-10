
def get_min_empty_squares(N):
    # Initialize variables
    min_empty_squares = float('inf')
    widgets_per_box = 0

    # Iterate through all possible box sizes
    for W in range(1, int(N ** 0.5) + 1):
        for H in range(W, 2 * W):
            # Calculate the number of widgets that can fit in a box of size W x H
            widgets_per_box = W * H

            # If the number of widgets is less than or equal to N, calculate the number of empty squares
            if widgets_per_box <= N:
                empty_squares = (W * H) - N

                # Update the minimum number of empty squares if necessary
                if empty_squares < min_empty_squares:
                    min_empty_squares = empty_squares

    return min_empty_squares

def main():
    N = int(input())
    print(get_min_empty_squares(N))

if __name__ == '__main__':
    main()

