
def get_painted_stones(k, x):
    # Find the range of coordinates that potentially contain a painted stone
    min_coord = x - k // 2
    max_coord = x + k // 2
    
    # Create a list to store the painted stone coordinates
    painted_stones = []
    
    # Iterate through the range of coordinates and check if they are painted black
    for i in range(min_coord, max_coord + 1):
        if i == x:
            painted_stones.append(i)
    
    return painted_stones

def main():
    # Read the input from stdin
    k, x = map(int, input().split())
    
    # Get the painted stone coordinates
    painted_stones = get_painted_stones(k, x)
    
    # Print the painted stone coordinates in ascending order
    print(*painted_stones)

if __name__ == '__main__':
    main()

