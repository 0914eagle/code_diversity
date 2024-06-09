
def get_enemy_spaceships(y_coordinates_1, y_coordinates_2):
    return len(set(y_coordinates_1)) + len(set(y_coordinates_2))

def get_destroyed_spaceships(y_coordinates_1, y_coordinates_2, x_coordinate):
    destroyed_spaceships = 0
    for y in y_coordinates_1:
        if y == x_coordinate:
            destroyed_spaceships += 1
    for y in y_coordinates_2:
        if y == x_coordinate:
            destroyed_spaceships += 1
    return destroyed_spaceships

def get_largest_number_of_destroyed_spaceships(y_coordinates_1, y_coordinates_2):
    largest_number_of_destroyed_spaceships = 0
    for x_coordinate in [-100, 100]:
        number_of_destroyed_spaceships = get_destroyed_spaceships(y_coordinates_1, y_coordinates_2, x_coordinate)
        if number_of_destroyed_spaceships > largest_number_of_destroyed_spaceships:
            largest_number_of_destroyed_spaceships = number_of_destroyed_spaceships
    return largest_number_of_destroyed_spaceships

def main():
    n, m = map(int, input().split())
    y_coordinates_1 = list(map(int, input().split()))
    y_coordinates_2 = list(map(int, input().split()))
    print(get_largest_number_of_destroyed_spaceships(y_coordinates_1, y_coordinates_2))

if __name__ == '__main__':
    main()

