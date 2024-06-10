
def get_painted_coordinates(k, x):
    # Find the range of coordinates that contain the painted stones
    start = x - k // 2
    end = x + k // 2
    
    # Create a list to store the painted coordinates
    painted_coordinates = []
    
    # Loop through the range of coordinates and check if the current coordinate is painted black
    for i in range(start, end + 1):
        if i == x:
            painted_coordinates.append(i)
    
    return painted_coordinates

def main():
    # Read the input from stdin
    k, x = map(int, input().split())
    
    # Call the get_painted_coordinates function and print the result
    painted_coordinates = get_painted_coordinates(k, x)
    print(*painted_coordinates)
    
if __name__ == '__main__':
    main()

