
def get_max_squares(colors):
    # Initialize variables
    max_squares = 0
    current_color = 1
    colors_used = [0] * (len(colors) + 1)

    # Iterate through each color
    for color in colors:
        # Check if there is enough paint of the current color
        if colors_used[current_color] + color <= colors_used[current_color - 1]:
            # If there is enough paint, use it and update the number of squares painted
            colors_used[current_color] += color
            max_squares += color
        else:
            # If there is not enough paint, switch to the next color and update the number of squares painted
            current_color += 1
            colors_used[current_color] += color
            max_squares += color

        # Wrap around to the first color if necessary
        if current_color == len(colors) + 1:
            current_color = 1

    return max_squares

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_max_squares(colors))

if __name__ == '__main__':
    main()

