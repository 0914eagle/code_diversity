
import math

def get_hit_enemies(opponents, angle):
    hit_enemies = 0
    for opponent in opponents:
        x, y, r = opponent
        dx, dy = math.cos(angle), math.sin(angle)
        A, B, C = dx**2 + dy**2, 2*(x*dx + y*dy), x**2 + y**2 - r**2
        discriminant = B**2 - 4*A*C
        if discriminant < 0:
            continue
        hit_enemies += 1
    return hit_enemies

def solve(opponents):
    max_hit_enemies = 0
    for angle in range(0, 360):
        hit_enemies = get_hit_enemies(opponents, angle/180*math.pi)
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

