
def get_max_squares(jars, colors):
    # Initialize variables
    max_squares = 0
    current_color = 1
    current_jar = 1
    jars_used = [0] * len(jars)

    # Loop through each jar and calculate the maximum number of squares that can be painted
    for i in range(len(jars)):
        # Calculate the number of squares that can be painted with the current color
        num_squares = min(jars[i], colors[current_color] - jars_used[current_color])

        # Update the maximum number of squares
        max_squares += num_squares

        # Update the jars used and the current color
        jars_used[current_color] += num_squares
        current_color = (current_color % len(jars)) + 1
        current_jar += 1

    return max_squares

def main():
    n = int(input())
    jars = list(map(int, input().split()))
    colors = [0] * (n + 1)
    for i in range(1, n + 1):
        colors[i] = sum(jars[i:])
    print(get_max_squares(jars, colors))

if __name__ == '__main__':
    main()

