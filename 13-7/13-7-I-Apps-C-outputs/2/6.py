
import math

def get_hit_enemies(x, y, r, opponents):
    hit_enemies = 0
    for opponent in opponents:
        dx, dy = x - opponent[0], y - opponent[1]
        if dx**2 + dy**2 <= r**2:
            hit_enemies += 1
    return hit_enemies

def get_optimal_angle(x, y, r, opponents):
    optimal_angle = 0
    max_hit_enemies = 0
    for angle in range(360):
        cx = x + r * math.cos(math.radians(angle))
        cy = y + r * math.sin(math.radians(angle))
        hit_enemies = get_hit_enemies(cx, cy, r, opponents)
        if hit_enemies > max_hit_enemies:
            max_hit_enemies = hit_enemies
            optimal_angle = angle
    return optimal_angle

def main():
    n = int(input())
    opponents = []
    for i in range(n):
        x, y, r = map(float, input().split())
        opponents.append([x, y, r])
    x, y, r = map(float, input().split())
    optimal_angle = get_optimal_angle(x, y, r, opponents)
    print(optimal_angle)

if __name__ == '__main__':
    main()

