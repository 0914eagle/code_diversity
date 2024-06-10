
import math

def is_overlapping(x1, y1, x2, y2):
    return x1 <= x2+1 and x2 <= x1+1 and y1 <= y2+1 and y2 <= y1+1

def get_energy_sum(lamps):
    positive_energy = 0
    negative_energy = 0
    for lamp in lamps:
        if lamp[2] > 0:
            positive_energy += lamp[2]
        else:
            negative_energy += lamp[2]
    return positive_energy, negative_energy

def get_closest_contiguous_sum(lamps, positive_energy, negative_energy):
    min_distance = math.inf
    for i in range(len(lamps)):
        for j in range(i+1, len(lamps)):
            distance = math.sqrt((lamps[i][0] - lamps[j][0]) ** 2 + (lamps[i][1] - lamps[j][1]) ** 2)
            if distance < min_distance and get_energy_sum(lamps[i:j+1]) == (positive_energy, negative_energy):
                min_distance = distance
    return min_distance

def get_shortest_contiguous_sum(lamps, positive_energy, negative_energy):
    min_distance = math.inf
    for i in range(len(lamps)):
        for j in range(i+1, len(lamps)):
            distance = math.sqrt((lamps[i][0] - lamps[j][0]) ** 2 + (lamps[i][1] - lamps[j][1]) ** 2)
            if distance < min_distance and get_energy_sum(lamps[i:j+1]) == (positive_energy, negative_energy):
                min_distance = distance
                shortest_lamps = lamps[i:j+1]
    return min_distance, shortest_lamps

def get_shortest_sum(lamps):
    positive_energy, negative_energy = get_energy_sum(lamps)
    if positive_energy == negative_energy:
        return 0
    elif positive_energy > negative_energy:
        return get_closest_contiguous_sum(lamps, positive_energy, negative_energy)
    else:
        return get_closest_contiguous_sum(lamps, negative_energy, positive_energy)

def get_shortest_line(lamps):
    shortest_distance, shortest_lamps = get_shortest_sum(lamps)
    if shortest_distance == math.inf:
        return "IMPOSSIBLE"
    else:
        return shortest_distance

def main():
    n = int(input())
    lamps = []
    for i in range(n):
        x, y, e = map(int, input().split())
        lamps.append([x, y, e])
    print(get_shortest_line(lamps))

if __name__ == '__main__':
    main()

