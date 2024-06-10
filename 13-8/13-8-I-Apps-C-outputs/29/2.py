
def get_energy_wasted(boxes, P):
    # Sort the boxes by probability in descending order
    sorted_boxes = sorted(boxes, key=lambda x: x[1], reverse=True)

    # Initialize the energy wasted and the probability of finding Polly
    energy_wasted = 0
    prob_found = 0

    # Loop through the boxes and add the energy wasted and the probability of finding Polly
    for box in sorted_boxes:
        energy_wasted += box[0]
        prob_found += box[1]

        # If the probability of finding Polly is greater than or equal to P, return the minimum energy wasted
        if prob_found >= P:
            return energy_wasted

    # If Polly was not found with at least probability P, return -1
    return -1

def main():
    N, P = map(int, input().split())
    boxes = []
    for _ in range(N):
        e, p = map(float, input().split())
        boxes.append((e, p))
    print(get_energy_wasted(boxes, P))

if __name__ == '__main__':
    main()

