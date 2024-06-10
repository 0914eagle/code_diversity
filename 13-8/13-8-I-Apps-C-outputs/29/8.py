
def get_min_energy(N, P, energy, probability):
    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(range(N), key=lambda i: probability[i], reverse=True)

    # Initialize the minimum energy to waste
    min_energy = 0

    # Iterate through the sorted boxes
    for i in sorted_boxes:
        # If the probability of finding Polly in the current box is greater than or equal to P, return the current energy waste
        if probability[i] >= P:
            return min_energy + energy[i]

        # Otherwise, add the energy waste for the current box and continue to the next box
        min_energy += energy[i]

    # If no box has a probability greater than or equal to P, return the total energy waste
    return min_energy

def main():
    N, P = map(int, input().split())
    energy = list(map(int, input().split()))
    probability = list(map(float, input().split()))
    print(get_min_energy(N, P, energy, probability))

if __name__ == '__main__':
    main()

