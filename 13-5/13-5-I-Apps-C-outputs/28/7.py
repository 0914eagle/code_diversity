
def get_enemy_spaceships(x_coord, y_coords):
    return [y for y in y_coords if y % x_coord == 0]

def get_destroyed_spaceships(x_coord, y_coords, positions):
    destroyed_spaceships = 0
    for position in positions:
        enemy_spaceships = get_enemy_spaceships(x_coord, y_coords)
        for enemy_spaceship in enemy_spaceships:
            if enemy_spaceship % position == 0:
                destroyed_spaceships += 1
                break
    return destroyed_spaceships

def get_largest_number_of_destroyed_spaceships(x_coords, y_coords):
    positions = set()
    for x_coord in x_coords:
        positions.add(x_coord)
    destroyed_spaceships = 0
    for position in positions:
        destroyed_spaceships = max(destroyed_spaceships, get_destroyed_spaceships(position, y_coords, positions))
    return destroyed_spaceships

def main():
    n, m = map(int, input().split())
    y_coords_1 = list(map(int, input().split()))
    y_coords_2 = list(map(int, input().split()))
    x_coords = [-100, 100]
    print(get_largest_number_of_destroyed_spaceships(x_coords, y_coords_1 + y_coords_2))

if __name__ == '__main__':
    main()

