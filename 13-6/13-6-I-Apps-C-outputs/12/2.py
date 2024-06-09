
import math

def get_input():
    N = int(input())
    stars = []
    for _ in range(N):
        T, s, a = map(float, input().split())
        stars.append((T, s, a))
    return N, stars

def get_distance(star, angle):
    T, s, a = star
    dist = math.fabs(angle - a)
    if dist > math.pi:
        dist = 2 * math.pi - dist
    return max(0, T - s * dist)

def get_max_distance(stars):
    max_distance = 0
    for star in stars:
        max_distance += get_distance(star, math.pi / 2)
    return max_distance

def f1():
    N, stars = get_input()
    return get_max_distance(stars)

def f2():
    N, stars = get_input()
    max_distance = 0
    for i in range(N):
        for j in range(i+1, N):
            star1 = stars[i]
            star2 = stars[j]
            angle = (star1[2] + star2[2]) / 2
            distance = get_distance(star1, angle) + get_distance(star2, angle)
            max_distance = max(max_distance, distance)
    return max_distance

if __name__ == '__main__':
    print(f1())
    print(f2())

