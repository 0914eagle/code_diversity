
def get_energy_contribution(x, y, e):
    return e

def get_line_length(lamps):
    # Sort lamps by their energy contribution in descending order
    lamps.sort(key=lambda x: x[2], reverse=True)

    # Initialize the total energy and the current line length
    total_energy = 0
    current_line_length = 0

    # Loop through the lamps and calculate the total energy and the current line length
    for lamp in lamps:
        total_energy += lamp[2]
        current_line_length += 1

        # If the total energy is equal to the sum of the energies outside the line, return the current line length
        if total_energy == sum([lamp[2] for lamp in lamps[current_line_length:]]) * 2:
            return current_line_length

    # If no line length is found, return IMPOSSIBLE
    return "IMPOSSIBLE"

def main():
    # Read the number of lamps
    n = int(input())

    # Read the lamps
    lamps = []
    for i in range(n):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))

    # Get the line length
    line_length = get_line_length(lamps)

    # Print the line length
    print(line_length)

if __name__ == '__main__':
    main()

