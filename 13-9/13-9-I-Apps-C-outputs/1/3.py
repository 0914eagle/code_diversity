
def get_wasted_paper(card_types, envelope_types):
    # Initialize variables
    total_wasted_paper = 0

    # Loop through each card type
    for card_type in card_types:
        # Find the smallest envelope that fits the card
        smallest_envelope = find_smallest_envelope(card_type, envelope_types)

        # Calculate the wasted paper for this card
        wasted_paper = calculate_wasted_paper(card_type, smallest_envelope)

        # Add the wasted paper to the total
        total_wasted_paper += wasted_paper

    return total_wasted_paper

def find_smallest_envelope(card_type, envelope_types):
    # Initialize variables
    smallest_envelope = None
    smallest_area = float('inf')

    # Loop through each envelope type
    for envelope_type in envelope_types:
        # Calculate the area of the envelope
        area = envelope_type[0] * envelope_type[1]

        # Check if the envelope fits the card
        if area >= card_type[0] * card_type[1]:
            # Check if the envelope is smaller than the current smallest envelope
            if area < smallest_area:
                # Update the smallest envelope
                smallest_envelope = envelope_type
                smallest_area = area

    return smallest_envelope

def calculate_wasted_paper(card_type, smallest_envelope):
    # Calculate the area of the card
    card_area = card_type[0] * card_type[1]

    # Calculate the area of the envelope
    envelope_area = smallest_envelope[0] * smallest_envelope[1]

    # Calculate the wasted paper
    wasted_paper = envelope_area - card_area

    return wasted_paper

def main():
    # Read the input
    n, k = map(int, input().split())
    card_types = []
    for i in range(n):
        w, h, q = map(int, input().split())
        card_types.append((w, h, q))

    # Find the smallest amount of wasted paper
    total_wasted_paper = get_wasted_paper(card_types, k)

    # Print the output
    print(total_wasted_paper)

if __name__ == '__main__':
    main()

