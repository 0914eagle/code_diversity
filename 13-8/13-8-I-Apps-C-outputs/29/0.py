
def get_min_energy(N, P, boxes):
    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(boxes, key=lambda x: x[1], reverse=True)

    # Initialize the minimum energy to spend and the current probability
    min_energy = 0
    current_probability = 0

    # Iterate through the sorted boxes
    for box in sorted_boxes:
        # Calculate the current probability of finding Polly
        current_probability += box[1]

        # If the current probability is greater than or equal to P, return the minimum energy
        if current_probability >= P:
            return min_energy

        # Otherwise, add the energy required to open the box and continue
        min_energy += box[0]

    # If all boxes have been checked and Polly has not been found, return -1
    return -1

def main():
    N, P = map(int, input().split())
    boxes = []
    for _ in range(N):
        energy, probability = map(float, input().split())
        boxes.append((energy, probability))
    print(get_min_energy(N, P, boxes))

if __name__ == '__main__':
    main()

