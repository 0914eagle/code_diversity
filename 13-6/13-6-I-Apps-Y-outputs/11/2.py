
def get_min_diff(h, w):
    # Initialize variables
    min_diff = float('inf')
    max_area = 0
    min_area = 0

    # Loop through all possible ways to divide the chocolate bar
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            # Calculate the area of the largest piece
            max_area = i * j

            # Calculate the area of the smallest piece
            min_area = (h - i) * (w - j)

            # Calculate the difference between the largest and smallest areas
            diff = max_area - min_area

            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff

    return min_diff

def main():
    # Read the input
    h, w = map(int, input().split())

    # Calculate the minimum difference
    min_diff = get_min_diff(h, w)

    # Print the result
    print(min_diff)

if __name__ == '__main__':
    main()

