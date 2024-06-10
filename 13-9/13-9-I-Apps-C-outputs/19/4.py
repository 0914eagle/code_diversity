
def get_light_positions(n):
    positions = []
    for i in range(n):
        x, y, e = map(int, input().split())
        positions.append((x, y, e))
    return positions

def get_light_energy(positions):
    total_energy = 0
    for x, y, e in positions:
        total_energy += e
    return total_energy

def get_light_balance_line(positions):
    total_energy = get_light_energy(positions)
    if total_energy == 0:
        return 0

    sorted_positions = sorted(positions, key=lambda x: x[2])
    negative_energy = 0
    for x, y, e in sorted_positions:
        if e < 0:
            negative_energy += e
        else:
            break

    if negative_energy == 0:
        return 0

    positive_energy = total_energy - negative_energy
    ratio = negative_energy / positive_energy

    for x, y, e in sorted_positions:
        if e > 0:
            break
        negative_energy -= e
        positive_energy -= e * ratio

    return get_light_balance_line_helper(positions, negative_energy, positive_energy)

def get_light_balance_line_helper(positions, negative_energy, positive_energy):
    if negative_energy == 0 or positive_energy == 0:
        return 0

    sorted_positions = sorted(positions, key=lambda x: x[2])
    for x, y, e in sorted_positions:
        if e > 0:
            break
        negative_energy -= e
        positive_energy -= e

    return get_light_balance_line_helper(positions, negative_energy, positive_energy)

def main():
    n = int(input())
    positions = get_light_positions(n)
    balance_line = get_light_balance_line(positions)
    print(balance_line)

if __name__ == '__main__':
    main()

