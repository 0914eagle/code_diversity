
import math

def get_angle(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    return angle

def get_hit_enemies(x, y, r, enemies):
    hit_enemies = 0
    for enemy in enemies:
        enemy_x, enemy_y, enemy_r = enemy
        distance = math.sqrt((x - enemy_x) ** 2 + (y - enemy_y) ** 2)
        if distance <= r + enemy_r:
            hit_enemies += 1
    return hit_enemies

def get_max_hit_enemies(enemies):
    max_hit_enemies = 0
    for enemy in enemies:
        enemy_x, enemy_y, enemy_r = enemy
        hit_enemies = get_hit_enemies(enemy_x, enemy_y, enemy_r, enemies)
        if hit_enemies > max_hit_enemies:
            max_hit_enemies = hit_enemies
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

