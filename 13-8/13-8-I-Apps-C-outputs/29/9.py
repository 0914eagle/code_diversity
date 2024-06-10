
def get_min_energy(N, P, energy, probability):
    # Initialize variables
    min_energy = 0
    total_probability = 0

    # Sort the boxes by energy in descending order
    sorted_boxes = sorted(range(N), key=lambda i: energy[i], reverse=True)

    # Iterate through the boxes
    for i in sorted_boxes:
        # If the total probability is greater than or equal to P, return the current minimum energy
        if total_probability >= P:
            return min_energy

        # Add the current energy to the minimum energy
        min_energy += energy[i]

        # Add the probability of the current box to the total probability
        total_probability += probability[i]

    # If the total probability is less than P, return -1
    return -1

def main():
    # Read the input
    N, P = map(int, input().split())
    energy = [int(x) for x in input().split()]
    probability = [float(x) for x in input().split()]

    # Call the get_min_energy function
    min_energy = get_min_energy(N, P, energy, probability)

    # Print the output
    print(min_energy)

if __name__ == '__main__':
    main()

