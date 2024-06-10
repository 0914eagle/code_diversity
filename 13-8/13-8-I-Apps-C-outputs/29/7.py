
def get_min_energy(N, P, energy_list, probability_list):
    # Initialize variables
    min_energy = 0
    total_probability = 0

    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(range(N), key=lambda i: probability_list[i], reverse=True)

    # Loop through the boxes and calculate the minimum energy needed
    for i in sorted_boxes:
        energy = energy_list[i]
        probability = probability_list[i]
        total_probability += probability

        if total_probability >= P:
            min_energy += energy
            break
        else:
            min_energy += energy

    return min_energy

def main():
    N, P = map(int, input().split())
    energy_list = []
    probability_list = []

    for i in range(N):
        energy, probability = map(float, input().split())
        energy_list.append(energy)
        probability_list.append(probability)

    min_energy = get_min_energy(N, P, energy_list, probability_list)
    print(min_energy)

if __name__ == '__main__':
    main()

