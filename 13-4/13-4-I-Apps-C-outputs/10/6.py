
def get_energy_contribution(x, y, energy):
    return energy

def get_line_length(lamp_positions, lamp_energies):
    # Your code here
    return 0.0

def main():
    num_lamp_positions = int(input())
    lamp_positions = []
    lamp_energies = []
    for i in range(num_lamp_positions):
        x, y, energy = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(get_energy_contribution(x, y, energy))
    line_length = get_line_length(lamp_positions, lamp_energies)
    print(line_length)

if __name__ == '__main__':
    main()

