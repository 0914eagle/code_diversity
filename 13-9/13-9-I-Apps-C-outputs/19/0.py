
def get_energy_contribution(lamps):
    positive_energy = 0
    negative_energy = 0
    for lamp in lamps:
        if lamp[2] > 0:
            positive_energy += lamp[2]
        else:
            negative_energy += lamp[2]
    return positive_energy, negative_energy

def get_balancing_line(lamps):
    positive_energy, negative_energy = get_energy_contribution(lamps)
    if positive_energy == negative_energy:
        return "IMPOSSIBLE"
    elif positive_energy > negative_energy:
        return "IMPOSSIBLE"
    else:
        balancing_line = []
        for i in range(len(lamps)):
            lamp = lamps[i]
            if lamp[2] < 0:
                continue
            for j in range(i+1, len(lamps)):
                other_lamp = lamps[j]
                if other_lamp[2] > 0:
                    continue
                if lamp[0] == other_lamp[0] and lamp[1] == other_lamp[1]:
                    continue
                if lamp[0] == other_lamp[0] and lamp[1] - other_lamp[1] == 1:
                    balancing_line.append(lamp)
                    break
                elif lamp[1] == other_lamp[1] and lamp[0] - other_lamp[0] == 1:
                    balancing_line.append(lamp)
                    break
        if len(balancing_line) == 0:
            return "IMPOSSIBLE"
        else:
            return balancing_line

def main():
    num_lamps = int(input())
    lamps = []
    for i in range(num_lamps):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    balancing_line = get_balancing_line(lamps)
    if balancing_line == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        balancing_line_length = 0
        for i in range(len(balancing_line)-1):
            lamp1 = balancing_line[i]
            lamp2 = balancing_line[i+1]
            balancing_line_length += abs(lamp1[0] - lamp2[0])
        print(balancing_line_length)

if __name__ == '__main__':
    main()

