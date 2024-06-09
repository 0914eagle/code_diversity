
def get_max_colors(n):
    # Initialize a set to store the colors
    colors = set()
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add the color to the set
            colors.add(i)
    # Return the length of the set
    return len(colors)

def main():
    n = int(input())
    print(get_max_colors(n))

if __name__ == '__main__':
    main()

