
def get_min_energy(N, P, energies, probabilities):
    # Initialize variables
    min_energy = 0
    total_probability = 0
    opened_boxes = []

    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(range(N), key=lambda i: probabilities[i], reverse=True)

    # Loop through the boxes and calculate the minimum energy needed to open them
    for i in sorted_boxes:
        if total_probability + probabilities[i] >= P:
            min_energy += energies[i]
            opened_boxes.append(i)
            total_probability += probabilities[i]
        else:
            break

    return min_energy

def main():
    N, P = map(int, input().split())
    energies = []
    probabilities = []
    for i in range(N):
        energy, probability = map(float, input().split())
        energies.append(energy)
        probabilities.append(probability)
    print(get_min_energy(N, P, energies, probabilities))

if __name__ == '__main__':
    main()

