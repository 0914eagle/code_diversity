
def find_polly(n, p, e, p_box):
    # Initialize variables
    min_energy = 0
    max_probability = 0
    selected_boxes = []

    # Loop through all boxes
    for i in range(n):
        # Check if the probability is greater than or equal to the minimum required probability
        if p_box[i] >= p:
            # Add the energy required to open the box to the minimum energy
            min_energy += e[i]
            # Add the probability of the box to the maximum probability
            max_probability += p_box[i]
            # Add the box to the selected boxes
            selected_boxes.append(i)

    # Return the minimum energy and the selected boxes
    return min_energy, selected_boxes

def main():
    # Read the input
    n, p = map(int, input().split())
    e = []
    p_box = []
    for i in range(n):
        ei, pi = map(float, input().split())
        e.append(ei)
        p_box.append(pi)

    # Find Polly
    min_energy, selected_boxes = find_polly(n, p, e, p_box)

    # Print the output
    print(min_energy)

if __name__ == '__main__':
    main()

