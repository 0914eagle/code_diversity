
def get_laser_destruction_count(enemy_spaceships, x_positions):
    # Find the maximum number of enemy spaceships that can be destroyed by laser shots from a given position
    max_destruction_count = 0
    for position in x_positions:
        destruction_count = 0
        for spaceship in enemy_spaceships:
            if spaceship[0] == position:
                destruction_count += 1
        max_destruction_count = max(max_destruction_count, destruction_count)
    return max_destruction_count

def get_best_positions(enemy_spaceships):
    # Find the best positions for the small spaceships to position themselves at
    x_positions = [-100, 100]
    best_destruction_count = 0
    for x_position in x_positions:
        destruction_count = get_laser_destruction_count(enemy_spaceships, [x_position])
        if destruction_count > best_destruction_count:
            best_destruction_count = destruction_count
            best_x_position = x_position
    return [best_x_position, best_destruction_count]

def main():
    n, m = map(int, input().split())
    enemy_spaceships = []
    for i in range(n):
        enemy_spaceships.append([-100, int(input())])
    for i in range(m):
        enemy_spaceships.append([100, int(input())])
    best_x_position, best_destruction_count = get_best_positions(enemy_spaceships)
    print(best_destruction_count)

if __name__ == '__main__':
    main()

