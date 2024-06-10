
def get_enemy_ships(n, m, y1, y2):
    enemy_ships = []
    for i in range(n):
        enemy_ships.append((-100, y1[i]))
    for i in range(m):
        enemy_ships.append((100, y2[i]))
    return enemy_ships

def get_destroyed_spaceships(enemy_ships, positions):
    destroyed_spaceships = 0
    for position in positions:
        for enemy_ship in enemy_ships:
            if enemy_ship[1] == position[1] and (enemy_ship[0] == position[0] or abs(enemy_ship[0] - position[0]) == 100):
                destroyed_spaceships += 1
                break
    return destroyed_spaceships

def solve(n, m, y1, y2):
    enemy_ships = get_enemy_ships(n, m, y1, y2)
    positions = [(0, y) for y in set(y1 + y2)]
    destroyed_spaceships = get_destroyed_spaceships(enemy_ships, positions)
    return destroyed_spaceships

if __name__ == '__main__':
    n, m = map(int, input().split())
    y1 = list(map(int, input().split()))
    y2 = list(map(int, input().split()))
    print(solve(n, m, y1, y2))

