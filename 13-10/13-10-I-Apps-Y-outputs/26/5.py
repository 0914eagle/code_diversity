
def get_coloring(a, b):
    # Initialize a dictionary to store the number of tiles of each color
    colors = {"red": a, "blue": b}
    # Initialize a list to store the perimeters of each possible coloring
    perimeters = []
    
    # Iterate over all possible ways to color the tiles
    for i in range(a + 1):
        for j in range(b + 1):
            # Check if the current coloring is valid
            if i + j == a + b and i <= a and j <= b:
                # Calculate the perimeter of the current coloring
                perimeter = 2 * (i + j)
                # Add the perimeter to the list of possible perimeters
                perimeters.append(perimeter)
    
    # Return the minimum perimeter
    return min(perimeters)

def main():
    # Read the input
    a, b = map(int, input().split())
    # Calculate the minimum perimeter
    perimeter = get_coloring(a, b)
    # Print the result
    print(perimeter)

if __name__ == '__main__':
    main()

