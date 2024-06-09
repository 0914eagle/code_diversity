
import math

def get_hit_enemies(x, y, r, opponents):
    hit_enemies = 0
    for opponent in opponents:
        if math.sqrt((x - opponent[0]) ** 2 + (y - opponent[1]) ** 2) <= r + opponent[2]:
            hit_enemies += 1
    return hit_enemies

def solve(n, opponents):
    max_hit_enemies = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = opponents[i]
            x2, y2, r2 = opponents[j]
            dx, dy = x2 - x1, y2 - y1
            d = math.sqrt(dx ** 2 + dy ** 2)
            if d <= r1 + r2:
                continue
            angle = math.acos(min(1, (r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d)))
            x, y = x1 + r1 * dx / d, y1 + r1 * dy / d
            hit_enemies = get_hit_enemies(x, y, r1, opponents)
            if hit_enemies > max_hit_enemies:
                max_hit_enemies = hit_enemies
    return max_hit_enemies

if __name__ == '__main__':
    n = int(input())
    opponents = []
    for i in range(n):
        x, y, r = map(float, input().split())
        opponents.append((x, y, r))
    print(solve(n, opponents))

