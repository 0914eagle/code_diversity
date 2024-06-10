
def get_destructible_spaceships(enemy_spaceships1, enemy_spaceships2):
    # Find the unique y-coordinates of the enemy spaceships
    y_coordinates1 = set(enemy_spaceships1)
    y_coordinates2 = set(enemy_spaceships2)
    
    # Initialize the maximum number of destructible spaceships to 0
    max_destructible_spaceships = 0
    
    # Iterate over all possible y-coordinates of the small spaceships
    for y in range(-10000, 10001):
        # Find the number of enemy spaceships that can be destroyed by the laser shots from the small spaceship at (0, y)
        num_destructible_spaceships = len(set(enemy_spaceships1).intersection(set([y - y_coordinate for y_coordinate in y_coordinates1]))) + len(set(enemy_spaceships2).intersection(set([y - y_coordinate for y_coordinate in y_coordinates2])))
        
        # Update the maximum number of destructible spaceships if necessary
        if num_destructible_spaceships > max_destructible_spaceships:
            max_destructible_spaceships = num_destructible_spaceships
    
    return max_destructible_spaceships

def main():
    # Read the input data
    enemy_spaceships1 = list(map(int, input().split()))
    enemy_spaceships2 = list(map(int, input().split()))
    
    # Find the largest number of enemy spaceships that can be destroyed
    max_destructible_spaceships = get_destructible_spaceships(enemy_spaceships1, enemy_spaceships2)
    
    # Print the result
    print(max_destructible_spaceships)

if __name__ == '__main__':
    main()

