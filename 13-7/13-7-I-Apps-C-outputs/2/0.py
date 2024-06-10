
import math

def get_angle(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    return angle

def get_hit_enemies(x, y, r, opponents):
    hit_enemies = 0
    for opponent in opponents:
        dx, dy = x - opponent[0], y - opponent[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance <= r:
            hit_enemies += 1
    return hit_enemies

def get_optimal_angle(opponents):
    x, y = 0, 0
    r = 1
    optimal_angle = 0
    max_hit_enemies = 0
    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            opponent1 = opponents[i]
            opponent2 = opponents[j]
            angle = get_angle(x, y, opponent1[0], opponent1[1])
            dx, dy = opponent2[0] - x, opponent2[1] - y
            distance = math.sqrt(dx**2 + dy**2)
            if distance <= r:
                continue
            angle_between_opponents = get_angle(opponent1[0], opponent1[1], opponent2[0], opponent2[1])
            angle_diff = abs(angle - angle_between_opponents)
            if angle_diff > math.pi/2:
                angle_diff = math.pi - angle_diff
            if angle_diff > math.pi/9:
                continue
            hit_enemies = get_hit_enemies(x, y, r, opponents)
            if hit_enemies > max_hit_enemies:
                max_hit_enemies = hit_enemies
                optimal_angle = angle
    return optimal_angle

def main():
    opponents = []
    for _ in range(int(input())):
        x, y, r = map(float, input().split())
        opponents.append([x, y, r])
    optimal_angle = get_optimal_angle(opponents)
    print(optimal_angle)

if __name__ == '__main__':
    main()

