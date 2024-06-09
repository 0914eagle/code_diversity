
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
            opponent1, opponent2 = opponents[i], opponents[j]
            dx, dy = opponent1[0] - opponent2[0], opponent1[1] - opponent2[1]
            distance = math.sqrt(dx**2 + dy**2)
            if distance == 0:
                continue
            angle = math.acos(dx / distance)
            if dy < 0:
                angle = 2 * math.pi - angle
            x = opponent1[0] + opponent1[2] * math.cos(angle)
            y = opponent1[1] + opponent1[2] * math.sin(angle)
            hit_enemies = get_hit_enemies(x, y, opponent1[2], opponents)
            max_hit_enemies = max(max_hit_enemies, hit_enemies)
    return max_hit_enemies

def f2(n, opponents):
    max_hit_enemies = 0
    for i in range(n):
        for j in range(i+1, n):
            opponent1, opponent2 = opponents[i], opponents[j]
            dx, dy = opponent1[0] - opponent2[0], opponent1[1] - opponent2[1]
            distance = math.sqrt(dx**2 + dy**2)
            if distance == 0:
                continue
            angle = math.acos(dx / distance)
            if dy < 0:
                angle = 2 * math.pi - angle
            x = opponent1[0] + opponent1[2] * math.cos(angle)
            y = opponent1[1] + opponent1[2] * math.sin(angle)
            hit_enemies = get_hit_enemies(x, y, opponent1[2], opponents)
            max_hit_enemies = max(max_hit_enemies, hit_enemies)
    return max_hit_enemies

if __name__ == '__main__':
    n = int(input())
    opponents = []
    for i in range(n):
        x, y, r = map(float, input().split())
        opponents.append([x, y, r])
    print(f1(n, opponents))
    print(f2(n, opponents))

