
def get_possible_destructions(y_coordinates1, y_coordinates2):
    # Sort the y-coordinates in both groups
    y_coordinates1.sort()
    y_coordinates2.sort()
    
    # Initialize the number of destructions to 0
    destructions = 0
    
    # Iterate over the y-coordinates in both groups
    for y1, y2 in zip(y_coordinates1, y_coordinates2):
        # If the y-coordinates are the same, increment the number of destructions
        if y1 == y2:
            destructions += 1
    
    # Return the number of destructions
    return destructions

def main():
    # Read the number of enemy spaceships in both groups
    n, m = map(int, input().split())
    
    # Read the y-coordinates of the enemy spaceships in both groups
    y_coordinates1 = list(map(int, input().split()))
    y_coordinates2 = list(map(int, input().split()))
    
    # Call the get_possible_destructions function and print the result
    print(get_possible_destructions(y_coordinates1, y_coordinates2))

if __name__ == '__main__':
    main()

