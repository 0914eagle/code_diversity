
def get_enemy_spaceships(x_coord, y_coordinates):
    return [(x_coord, y) for y in y_coordinates]

def get_largest_destroyed_spaceships(enemy_spaceships):
    destroyed_spaceships = 0
    for spaceship in enemy_spaceships:
        if spaceship[0] == 0 and spaceship[1] > 0:
            destroyed_spaceships += 1
    return destroyed_spaceships

def main():
    n, m = map(int, input().split())
    y_coordinates_1 = list(map(int, input().split()))
    y_coordinates_2 = list(map(int, input().split()))
    enemy_spaceships_1 = get_enemy_spaceships(-100, y_coordinates_1)
    enemy_spaceships_2 = get_enemy_spaceships(100, y_coordinates_2)
    destroyed_spaceships_1 = get_largest_destroyed_spaceships(enemy_spaceships_1)
    destroyed_spaceships_2 = get_largest_destroyed_spaceships(enemy_spaceships_2)
    print(max(destroyed_spaceships_1, destroyed_spaceships_2))

if __name__ == '__main__':
    main()

