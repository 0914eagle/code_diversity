
import math

def get_hit_enemies(opponents, angle):
    hit_enemies = 0
    for opponent in opponents:
        x, y, r = opponent
        dist = math.sqrt((x - math.cos(angle)) ** 2 + (y - math.sin(angle)) ** 2)
        if dist <= r:
            hit_enemies += 1
    return hit_enemies

def solve(opponents):
    max_hit_enemies = 0
    for angle in range(360):
        hit_enemies = get_hit_enemies(opponents, angle)
        if hit_enemies > max_hit_enemies:
            max_hit_enemies = hit_enemies
    return max_hit_enemies

if __name__ == '__main__':
    n = int(input())
    opponents = []
    for _ in range(n):
        x, y, r = map(float, input().split())
        opponents.append((x, y, r))
    print(solve(opponents))

