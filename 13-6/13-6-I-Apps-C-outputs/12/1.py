
import math

def get_input():
    N = int(input())
    stars = []
    for _ in range(N):
        T, s, a = map(float, input().split())
        stars.append((T, s, a))
    return stars

def get_max_distance(stars):
    max_distance = 0
    for T, s, a in stars:
        distance = T - s * math.fabs(a - math.pi/2)
        if distance > max_distance:
            max_distance = distance
    return max_distance

def main():
    stars = get_input()
    print(get_max_distance(stars))

if __name__ == '__main__':
    main()

