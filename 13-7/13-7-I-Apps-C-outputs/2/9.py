
import math

def get_angle(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    return angle

def get_hit_enemies(x, y, radius, enemies):
    hit_enemies = []
    for enemy in enemies:
        dx = enemy[0] - x
        dy = enemy[1] - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance <= radius:
            hit_enemies.append(enemy)
    return hit_enemies

def get_max_hit_enemies(enemies):
    max_hit_enemies = 0
    for enemy in enemies:
        hit_enemies = get_hit_enemies(0, 0, enemy[2], enemies)
        if len(hit_enemies) > max_hit_enemies:
            max_hit_enemies = len(hit_enemies)
    return max_hit_enemies

def main():
    n = int(input())
    enemies = []
    for i in range(n):
        x, y, r = map(float, input().split())
        enemies.append((x, y, r))
    print(get_max_hit_enemies(enemies))

if __name__ == '__main__':
    main()

