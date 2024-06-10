
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def velocity(distance, time, m):
    return distance / time * m

def solve(n, mice, m):
    min_velocity = float('inf')
    for i in range(n):
        mouse = mice[i]
        distance = distance(0, 0, mouse[0], mouse[1])
        time = mouse[2]
        velocity_needed = velocity(distance, time, m)
        if velocity_needed < min_velocity:
            min_velocity = velocity_needed
    return min_velocity

def main():
    n = int(input())
    mice = []
    for i in range(n):
        x, y, s = map(int, input().split())
        mice.append([x, y, s])
    m = float(input())
    print(solve(n, mice, m))

if __name__ == '__main__':
    main()

