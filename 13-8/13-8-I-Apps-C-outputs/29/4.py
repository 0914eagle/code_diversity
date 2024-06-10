
def get_energy_wasted(probabilities, energy_required, minimum_probability):
    
    # Initialize variables
    total_energy = 0
    total_probability = 0

    # Iterate through the boxes
    for i in range(len(probabilities)):
        # Calculate the total probability and energy
        total_probability += probabilities[i]
        total_energy += energy_required[i]

        # If the total probability is greater than the minimum required probability, return the total energy wasted
        if total_probability >= minimum_probability:
            return total_energy

    # If the total probability is less than the minimum required probability, return -1
    return -1

def main():
    # Read the input
    num_boxes, minimum_probability = map(int, input().split())
    probabilities = []
    energy_required = []
    for _ in range(num_boxes):
        energy, probability = map(float, input().split())
        probabilities.append(probability)
        energy_required.append(energy)

    # Calculate the minimum energy wasted
    minimum_energy = get_energy_wasted(probabilities, energy_required, minimum_probability)

    # Print the output
    print(minimum_energy)

if __name__ == '__main__':
    main()

