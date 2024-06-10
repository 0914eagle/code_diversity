
def read_input():
    A, H = map(int, input().split())
    n, m = map(int, input().split())
    passages = []
    for _ in range(m):
        ei, bi, ai, hi = map(int, input().split())
        passages.append((ei, bi, ai, hi))
    return A, H, n, m, passages

def get_path(A, H, n, m, passages):
    # Initialize the graph with the passages
    graph = {i: set() for i in range(1, n + 1)}
    for ei, bi, _, _ in passages:
        graph[ei].add(bi)
    
    # Breadth-first search to find the shortest path from 1 to n
    queue = [(1, [1], 0)]
    visited = set()
    while queue:
        current, path, cost = queue.pop(0)
        if current == n:
            return path, cost
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], cost + 1))
        visited.add(current)
    
    return None, None

def fight(A, H, enemy_attack, enemy_health):
    while A > 0 and enemy_health > 0:
        A -= enemy_attack
        enemy_health -= H
    if enemy_health <= 0:
        return True
    else:
        return False

def solve(A, H, n, m, passages):
    path, cost = get_path(A, H, n, m, passages)
    if not path:
        return "Oh no"
    
    # Fight the enemies along the path
    enemies = [0] * (n + 1)
    for i in range(1, len(path)):
        ei, bi = path[i - 1], path[i]
        if enemies[ei] == 0:
            enemies[ei] = 1
        if enemies[bi] == 0:
            enemies[bi] = 1
        if fight(A, H, enemies[ei], enemies[bi]):
            enemies[bi] = 0
    
    return max(H - sum(enemies[1:]), 0)

if __name__ == '__main__':
    A, H, n, m, passages = read_input()
    print(solve(A, H, n, m, passages))

