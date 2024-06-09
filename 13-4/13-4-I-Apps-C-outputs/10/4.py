
import math

def get_energy_contribution(x, y, e):
    return e

def get_lamp_coordinates(x, y):
    return (x-1, y-1, x+1, y+1)

def get_lamp_area(x, y):
    return (x-1) * (y-1)

def get_lamp_energy(x, y, e):
    return e * get_lamp_area(x, y)

def get_total_energy(lamps):
    total_energy = 0
    for lamp in lamps:
        total_energy += get_lamp_energy(lamp[0], lamp[1], lamp[2])
    return total_energy

def get_balancing_line(lamps):
    total_energy = get_total_energy(lamps)
    if total_energy == 0:
        return 0
    
    balancing_line = 0
    for i in range(len(lamps)):
        for j in range(i+1, len(lamps)):
            lamp1 = lamps[i]
            lamp2 = lamps[j]
            x1, y1, x2, y2 = get_lamp_coordinates(lamp1[0], lamp1[1])
            x3, y3, x4, y4 = get_lamp_coordinates(lamp2[0], lamp2[1])
            area1 = get_lamp_area(x1, y1)
            area2 = get_lamp_area(x2, y2)
            area3 = get_lamp_area(x3, y3)
            area4 = get_lamp_area(x4, y4)
            energy1 = get_lamp_energy(x1, y1, lamp1[2])
            energy2 = get_lamp_energy(x2, y2, lamp1[2])
            energy3 = get_lamp_energy(x3, y3, lamp2[2])
            energy4 = get_lamp_energy(x4, y4, lamp2[2])
            total_energy1 = energy1 + energy2
            total_energy2 = energy3 + energy4
            if total_energy1 == total_energy2:
                balancing_line = max(balancing_line, abs(x1-x3) + abs(y1-y3))
                balancing_line = max(balancing_line, abs(x2-x4) + abs(y2-y4))
    
    return balancing_line

def main():
    num_lamps = int(input())
    lamps = []
    for i in range(num_lamps):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    
    balancing_line = get_balancing_line(lamps)
    if balancing_line == 0:
        print("IMPOSSIBLE")
    else:
        print(balancing_line)

if __name__ == '__main__':
    main()

