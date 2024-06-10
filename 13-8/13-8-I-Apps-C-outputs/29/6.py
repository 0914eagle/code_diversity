
def get_min_energy(N, P, energies, probabilities):
    # Initialize variables
    min_energy = 0
    total_probability = 0
    checked_boxes = 0

    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(range(N), key=lambda i: probabilities[i], reverse=True)

    # Iterate through the boxes and calculate the minimum energy required to find Polly with at least probability P
    for i in sorted_boxes:
        total_probability += probabilities[i]
        checked_boxes += 1
        if total_probability >= P:
            min_energy += energies[i]
            break
        else:
            min_energy += energies[i]

    return min_energy

def main():
    N, P = map(int, input().split())
    energies = list(map(int, input().split()))
    probabilities = list(map(float, input().split()))
    print(get_min_energy(N, P, energies, probabilities))

if __name__ == '__main__':
    main()

