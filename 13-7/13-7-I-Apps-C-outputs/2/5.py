
import math

def get_hit_enemies(x, y, r, opponents):
    hit_enemies = 0
    for opponent in opponents:
        if math.sqrt((x - opponent[0]) ** 2 + (y - opponent[1]) ** 2) <= r + opponent[2]:
            hit_enemies += 1
    return hit_enemies

def solve(opponents):
    max_hit_enemies = 0
    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            x1, y1, r1 = opponents[i]
            x2, y2, r2 = opponents[j]
            dx, dy = x2 - x1, y2 - y1
            d = math.sqrt(dx ** 2 + dy ** 2)
            if d <= r1 + r2:
                continue
            a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
            h = math.sqrt(r1 ** 2 - a ** 2)
            x0 = x1 + a * dx / d
            y0 = y1 + a * dy / d
            angle = math.atan2(dy, dx)
            for angle in [angle - 0.00000001, angle, angle + 0.00000001]:
                x = x0 + h * math.cos(angle)
                y = y0 + h * math.sin(angle)
                hit_enemies = get_hit_enemies(x, y, r1, opponents)
                max_hit_enemies = max(max_hit_enemies, hit_enemies)
    return max_hit_enemies

if __name__ == '__main__':
    n = int(input())
    opponents = []
    for _ in range(n):
        x, y, r = map(float, input().split())
        opponents.append((x, y, r))
    print(solve(opponents))

