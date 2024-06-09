
def get_maximum_colors(n):
    # Initialize a set to store the colors
    colors = set()
    # Iterate through all possible pairs of tiles
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the difference between the two tiles is a divisor of n greater than 1,
            # and n mod the difference is 0, then they should have the same color
            if n % abs(i - j) == 0 and abs(i - j) > 1:
                colors.add(i)
    return len(colors)

def main():
    n = int(input())
    print(get_maximum_colors(n))

if __name__ == '__main__':
    main()

