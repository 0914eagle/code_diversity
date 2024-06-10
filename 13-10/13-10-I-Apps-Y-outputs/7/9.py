
def get_black_stones(K, X):
    # Find the range of coordinates that potentially contain a stone painted black
    start = X - K // 2
    end = X + K // 2

    # Create a list to store the coordinates
    black_stones = []

    # Add the coordinates to the list
    for i in range(start, end + 1):
        black_stones.append(i)

    return black_stones

def main():
    # Read the input from stdin
    K, X = map(int, input().split())

    # Call the function to get the coordinates of the black stones
    black_stones = get_black_stones(K, X)

    # Print the coordinates in ascending order
    for stone in sorted(black_stones):
        print(stone, end=" ")

if __name__ == '__main__':
    main()

