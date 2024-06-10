
import itertools

def read_input():
    N = int(input())
    lamps = []
    for _ in range(N):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    return N, lamps

def find_balance_line(lamps):
    # sort lamps by x-coordinate
    lamps = sorted(lamps, key=lambda x: x[0])
    
    # find the shortest distance between two lamps
    min_dist = float('inf')
    for i in range(len(lamps) - 1):
        dist = abs(lamps[i + 1][0] - lamps[i][0])
        if dist < min_dist:
            min_dist = dist
    
    # find the position of the balance line
    for x in range(min_dist, 100):
        positive_energy = 0
        negative_energy = 0
        for lamp in lamps:
            if lamp[0] < x:
                positive_energy += lamp[2]
            else:
                negative_energy += lamp[2]
        if positive_energy == negative_energy:
            return x
    
    return "IMPOSSIBLE"

def main():
    N, lamps = read_input()
    print(find_balance_line(lamps))

if __name__ == '__main__':
    main()

