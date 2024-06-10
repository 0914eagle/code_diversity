
def get_black_stones(k, x):
    # Find the range of coordinates that potentially contain a black stone
    min_coord = x - k // 2
    max_coord = x + k // 2
    
    # Create a list to store the coordinates of the black stones
    black_stones = []
    
    # Iterate through the range of coordinates and check if the stone at that coordinate is black
    for coord in range(min_coord, max_coord + 1):
        if coord == x or (coord - x) % k == 0:
            black_stones.append(coord)
    
    return black_stones

def main():
    # Read the input from stdin
    k, x = map(int, input().split())
    
    # Call the function to get the coordinates of the black stones
    black_stones = get_black_stones(k, x)
    
    # Print the coordinates of the black stones
    print(*black_stones)
    
if __name__ == '__main__':
    main()

