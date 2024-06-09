
import math

def get_hit_enemies(x, y, r, opponents):
    hit_enemies = 0
    for opponent in opponents:
        if math.sqrt((x - opponent[0]) ** 2 + (y - opponent[1]) ** 2) <= r + opponent[2]:
            hit_enemies += 1
    return hit_enemies

def f1(n, opponents):
    max_hit_enemies = 0
    for i in range(n):
        for j in range(i + 1, n):
            hit_enemies = get_hit_enemies(opponents[i][0], opponents[i][1], opponents[i][2], opponents[j:])
            max_hit_enemies = max(max_hit_enemies, hit_enemies)
    return max_hit_enemies

def f2(n, opponents):
    max_hit_enemies = 0
    for i in range(n):
        for j in range(i + 1, n):
            hit_enemies = get_hit_enemies(opponents[i][0], opponents[i][1], opponents[i][2], opponents[j:])
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

