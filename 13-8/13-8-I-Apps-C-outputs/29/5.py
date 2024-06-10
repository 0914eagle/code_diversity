
def get_min_energy(boxes, probability):
    
    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(boxes, key=lambda x: x[1], reverse=True)

    # Initialize the minimum energy needed to find Polly
    min_energy = 0

    # Loop through the boxes and add the energy needed to open each box
    for box in sorted_boxes:
        min_energy += box[0]

        # If the current probability is greater than or equal to the minimum probability, return the current minimum energy
        if box[1] >= probability:
            return min_energy

    # If no box has a probability greater than or equal to the minimum probability, return the total minimum energy needed to open all the boxes
    return min_energy

def main():
    num_boxes, probability = map(float, input().split())
    boxes = []
    for _ in range(num_boxes):
        energy, probability = map(float, input().split())
        boxes.append((energy, probability))
    print(get_min_energy(boxes, probability))

if __name__ == '__main__':
    main()

