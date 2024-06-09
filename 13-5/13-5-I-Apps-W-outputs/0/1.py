
def get_max_squares(colors):
    # Initialize variables
    max_squares = 0
    current_color = 1
    colors_used = [0] * (len(colors) + 1)

    # Loop through each color and calculate the maximum number of squares that can be painted
    for color in colors:
        colors_used[current_color] += color
        max_squares += min(colors_used[current_color], color)
        current_color = (current_color + 1) % (len(colors) + 1)

    return max_squares

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    print(get_max_squares(colors))

if __name__ == '__main__':
    main()

