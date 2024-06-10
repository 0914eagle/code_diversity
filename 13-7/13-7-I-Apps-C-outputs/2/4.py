
import math

def get_opponents(n):
    opponents = []
    for i in range(n):
        x, y, r = map(float, input().split())
        opponents.append((x, y, r))
    return opponents

def get_max_hit_opponents(opponents):
    max_hit = 0
    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            x1, y1, r1 = opponents[i]
            x2, y2, r2 = opponents[j]
            dx, dy = x2-x1, y2-y1
            d = math.sqrt(dx**2 + dy**2)
            if d <= r1 + r2:
                max_hit += 1
    return max_hit

def main():
    n = int(input())
    opponents = get_opponents(n)
    max_hit = get_max_hit_opponents(opponents)
    print(max_hit)

if __name__ == '__main__':
    main()

