
import math

def get_attack_area(center, radius):
    
    return math.pi * radius ** 2

def get_intersection_area(circle1, circle2):
    
    dx, dy = circle1["center"][0] - circle2["center"][0], circle1["center"][1] - circle2["center"][1]
    dist = math.sqrt(dx ** 2 + dy ** 2)
    if dist > circle1["radius"] + circle2["radius"]:
        return 0
    if dist < abs(circle1["radius"] - circle2["radius"]):
        return 0
    if dist == 0 and circle1["radius"] == circle2["radius"]:
        return math.pi * circle1["radius"] ** 2
    if dist == 0 and circle1["radius"] != circle2["radius"]:
        return 0
    a = (circle1["radius"] ** 2 - circle2["radius"] ** 2 + dist ** 2) / (2 * dist)
    h = math.sqrt(circle1["radius"] ** 2 - a ** 2)
    area = circle1["radius"] ** 2 * math.acos(a / circle1["radius"]) + circle2["radius"] ** 2 * math.acos((circle1["radius"] - a) / circle2["radius"]) - 2 * a * h
    return area

def get_max_destroyable_minions(villages, minions, attack_radius):
    
    attack_area = get_attack_area((0, 0), attack_radius)
    for village in villages:
        village_area = get_attack_area(village["center"], village["radius"])
        intersect_area = get_intersection_area({"center": (0, 0), "radius": attack_radius}, village)
        if intersect_area >= village_area:
            return 0
        attack_area -= intersect_area
    return sum(minion in get_attack_area((0, 0), attack_radius) for minion in minions)

def main():
    num_villages, num_minions, attack_radius = map(int, input().split())
    villages = []
    for _ in range(num_villages):
        villages.append({"center": tuple(map(int, input().split())), "radius": int(input())})
    minions = set(tuple(map(int, input().split())) for _ in range(num_minions))
    print(get_max_destroyable_minions(villages, minions, attack_radius))

if __name__ == '__main__':
    main()

