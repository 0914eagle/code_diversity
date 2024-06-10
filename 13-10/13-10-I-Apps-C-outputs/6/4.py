
def get_enemy_information(n, m, enemy_info):
    enemies = {}
    for i in range(m):
        enemy = enemy_info[i]
        enemies[enemy[0]] = (enemy[1], enemy[2])
    return enemies

def get_safe_areas(n, m, passages):
    safe_areas = set()
    for passage in passages:
        safe_areas.add(passage[0])
        safe_areas.add(passage[1])
    return safe_areas

def find_shortest_path(start, end, enemies, visited, safe_areas):
    if start == end:
        return 0
    if start in visited:
        return float('inf')
    visited.add(start)
    shortest_path = float('inf')
    for enemy in enemies:
        if enemy in safe_areas:
            continue
        attack, health = enemies[enemy]
        if attack >= health:
            continue
        path = find_shortest_path(enemy, end, enemies, visited, safe_areas)
        if path < attack:
            shortest_path = min(shortest_path, path + health)
    return shortest_path

def solve(A, H, n, m, enemy_info):
    enemies = get_enemy_information(n, m, enemy_info)
    safe_areas = get_safe_areas(n, m, enemy_info)
    visited = set()
    shortest_path = find_shortest_path(1, n, enemies, visited, safe_areas)
    if shortest_path == float('inf'):
        return 'Oh no'
    return max(0, H - shortest_path)

if __name__ == '__main__':
    A, H = map(int, input().split())
    n, m = map(int, input().split())
    enemy_info = [list(map(int, input().split())) for _ in range(m)]
    print(solve(A, H, n, m, enemy_info))

