
import math

def get_attack_range(radius, villages):
    
    max_range = 0
    for village in villages:
        village_center = (village[0], village[1])
        village_radius = village[2]
        distance = math.sqrt((village_center[0] - radius) ** 2 + (village_center[1] - radius) ** 2)
        if distance + village_radius > max_range:
            max_range = distance + village_radius
    return max_range

def get_max_minions_destroyed(villages, minions, attack_radius):
    
    max_minions_destroyed = 0
    for village in villages:
        village_center = (village[0], village[1])
        village_radius = village[2]
        in_range_minions = []
        for minion in minions:
            distance = math.sqrt((minion[0] - village_center[0]) ** 2 + (minion[1] - village_center[1]) ** 2)
            if distance <= attack_radius and distance >= village_radius:
                in_range_minions.append(minion)
        if len(in_range_minions) > max_minions_destroyed:
            max_minions_destroyed = len(in_range_minions)
    return max_minions_destroyed

def main():
    n, m, r = map(int, input().split())
    villages = []
    for _ in range(n):
        village = list(map(int, input().split()))
        villages.append(village)
    minions = []
    for _ in range(m):
        minion = list(map(int, input().split()))
        minions.append(minion)
    attack_radius = get_attack_range(r, villages)
    max_minions_destroyed = get_max_minions_destroyed(villages, minions, attack_radius)
    print(max_minions_destroyed)

if __name__ == '__main__':
    main()

