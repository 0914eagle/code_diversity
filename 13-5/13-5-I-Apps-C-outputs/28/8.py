
def get_enemy_spaceships(y_coordinates, x_coordinate):
    return [SpaceShip(y, x_coordinate) for y in y_coordinates]

def get_largest_number_of_destroyed_spaceships(enemy_spaceships):
    destroyed_spaceships = 0
    for enemy_spaceship in enemy_spaceships:
        if enemy_spaceship.x == 0:
            destroyed_spaceships += 1
    return destroyed_spaceships

def main():
    n, m = map(int, input().split())
    y_coordinates_1 = list(map(int, input().split()))
    y_coordinates_2 = list(map(int, input().split()))
    enemy_spaceships_1 = get_enemy_spaceships(y_coordinates_1, -100)
    enemy_spaceships_2 = get_enemy_spaceships(y_coordinates_2, 100)
    largest_number_of_destroyed_spaceships = max(get_largest_number_of_destroyed_spaceships(enemy_spaceships_1), get_largest_number_of_destroyed_spaceships(enemy_spaceships_2))
    print(largest_number_of_destroyed_spaceships)

class SpaceShip:
    def __init__(self, y, x):
        self.y = y
        self.x = x

if __name__ == '__main__':
    main()

