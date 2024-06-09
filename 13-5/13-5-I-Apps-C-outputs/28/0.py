
def get_enemy_spaceships_to_destroy(x_coordinates, y_coordinates):
    # Sort the y_coordinates in ascending order
    sorted_y_coordinates = sorted(y_coordinates)
    
    # Initialize a set to store the unique y-coordinates
    unique_y_coordinates = set()
    
    # Iterate through the sorted y_coordinates and add them to the set
    for y in sorted_y_coordinates:
        unique_y_coordinates.add(y)
    
    # Return the length of the set, which is the number of unique y-coordinates
    return len(unique_y_coordinates)

def solve(n, m, y1, y2):
    # Get the enemy spaceships to destroy for the first group
    enemy_spaceships_to_destroy_1 = get_enemy_spaceships_to_destroy(x_coordinates=-100, y_coordinates=y1)
    
    # Get the enemy spaceships to destroy for the second group
    enemy_spaceships_to_destroy_2 = get_enemy_spaceships_to_destroy(x_coordinates=100, y_coordinates=y2)
    
    # Return the maximum number of enemy spaceships to destroy
    return max(enemy_spaceships_to_destroy_1, enemy_spaceships_to_destroy_2)

if __name__ == '__main__':
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    print(solve(n, m, y1, y2))

