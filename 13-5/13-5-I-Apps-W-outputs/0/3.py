
def get_max_squares(colors):
    # Initialize variables
    max_squares = 0
    current_color = 1
    remaining_colors = colors

    # Iterate through the colors
    for color in colors:
        # If there is enough paint of the current color, paint the next square
        if color >= current_color:
            max_squares += 1
            current_color += 1
            remaining_colors -= 1
        # If there is not enough paint of the current color, stop painting
        else:
            break

    # If all the colors have been used, paint the remaining squares with the first color
    if remaining_colors == 0:
        max_squares += len(colors)

    return max_squares

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_max_squares(colors))

if __name__ == '__main__':
    main()

