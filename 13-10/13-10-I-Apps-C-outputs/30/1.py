
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def check_intersection(center_x, center_y, radius, village_x, village_y, village_radius):
    distance = calculate_distance(center_x, center_y, village_x, village_y)
    return distance + radius >= village_radius and distance - radius <= village_radius

def get_max_minions(n, m, r, villages, minions):
    max_minions = 0
    for i in range(n):
        for j in range(m):
            if not check_intersection(villages[i][0], villages[i][1], villages[i][2], minions[j][0], minions[j][1], r):
                max_minions += 1
    return max_minions

def main():
    n, m, r = map(int, input().split())
    villages = []
    for i in range(n):
        village = list(map(int, input().split()))
        villages.append(village)
    minions = []
    for i in range(m):
        minion = list(map(int, input().split()))
        minions.append(minion)
    print(get_max_minions(n, m, r, villages, minions))

if __name__ == '__main__':
    main()

