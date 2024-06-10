
def get_enemy_spaceships_destroyed(y1, y2):
    # Sort the y-coordinates of the enemy spaceships
    y1.sort()
    y2.sort()
    
    # Initialize the number of destroyed enemy spaceships to 0
    destroyed_spaceships = 0
    
    # Iterate through the y-coordinates of the enemy spaceships
    for i in range(len(y1)):
        # Check if the current y-coordinate is common to both groups
        if y1[i] in y2:
            # If it is, increment the number of destroyed enemy spaceships
            destroyed_spaceships += 1
    
    # Return the number of destroyed enemy spaceships
    return destroyed_spaceships

def main():
    # Read the number of enemy spaceships with x = -100 and x = 100
    n, m = map(int, input().split())
    
    # Read the y-coordinates of the enemy spaceships
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    
    # Call the get_enemy_spaceships_destroyed function to get the number of destroyed enemy spaceships
    destroyed_spaceships = get_enemy_spaceships_destroyed(y1, y2)
    
    # Print the number of destroyed enemy spaceships
    print(destroyed_spaceships)

if __name__ == '__main__':
    main()

