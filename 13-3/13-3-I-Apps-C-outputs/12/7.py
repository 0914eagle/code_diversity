
import math

def get_hit_enemies(x, y, r, opponents):
    hit_enemies = 0
    for opponent in opponents:
        dx, dy = x - opponent[0], y - opponent[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance <= r and distance > 0:
            hit_enemies += 1
    return hit_enemies

def f1(n, opponents):
    max_hit_enemies = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = opponents[i]
            x2, y2, r2 = opponents[j]
            dx, dy = x2 - x1, y2 - y1
            distance = math.sqrt(dx**2 + dy**2)
            if distance <= r1 + r2:
                hit_enemies = get_hit_enemies(x1, y1, r1, opponents[i+1:]) + get_hit_enemies(x2, y2, r2, opponents[:i] + opponents[i+1:])
                max_hit_enemies = max(max_hit_enemies, hit_enemies)
    return max_hit_enemies

def f2(n, opponents):
    max_hit_enemies = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = opponents[i]
            x2, y2, r2 = opponents[j]
            dx, dy = x2 - x1, y2 - y1
            distance = math.sqrt(dx**2 + dy**2)
            if distance <= r1 + r2:
                hit_enemies = get_hit_enemies(x1, y1, r1, opponents[i+1:]) + get_hit_enemies(x2, y2, r2, opponents[:i] + opponents[i+1:])
                max_hit_enemies = max(max_hit_enemies, hit_enemies)
    return max_hit_enemies

if __name__ == '__main__':
    n = int(input())
    opponents = []
    for i in range(n):
        x, y, r = map(float, input().split())
        opponents.append((x, y, r))
    print(f1(n, opponents))
    print(f2(n, opponents))

