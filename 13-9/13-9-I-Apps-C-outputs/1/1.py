
def get_wasted_paper(card_types, envelope_types):
    # Initialize variables
    wasted_paper = 0
    envelopes = {}

    # Iterate through the card types
    for card_type in card_types:
        # Check if the current card type is already assigned to an envelope
        if card_type not in envelopes:
            # If not, find the smallest envelope that can fit the current card type
            smallest_envelope = find_smallest_envelope(card_type, envelope_types)
            # Add the card type to the envelope
            envelopes[card_type] = smallest_envelope
        # Calculate the wasted paper for the current card type
        wasted_paper += calculate_wasted_paper(card_type, envelopes[card_type])

    return wasted_paper

def find_smallest_envelope(card_type, envelope_types):
    # Initialize variables
    smallest_envelope = None
    smallest_area = float('inf')

    # Iterate through the envelope types
    for envelope_type in envelope_types:
        # Calculate the area of the current envelope type
        area = envelope_type[0] * envelope_type[1]
        # Check if the current envelope type is smaller than the smallest envelope found so far
        if area < smallest_area:
            # If it is, set it as the new smallest envelope
            smallest_envelope = envelope_type
            smallest_area = area

    return smallest_envelope

def calculate_wasted_paper(card_type, envelope_type):
    # Calculate the area of the card type
    card_area = card_type[0] * card_type[1]
    # Calculate the area of the envelope type
    envelope_area = envelope_type[0] * envelope_type[1]
    # Calculate the wasted paper
    wasted_paper = envelope_area - card_area

    return wasted_paper

def main():
    # Read the input
    card_types = []
    envelope_types = []
    for _ in range(int(input())):
        card_types.append(list(map(int, input().split())))
    envelope_types = [list(map(int, input().split())) for _ in range(int(input()))]

    # Call the function to get the wasted paper
    wasted_paper = get_wasted_paper(card_types, envelope_types)

    # Print the output
    print(wasted_paper)

if __name__ == '__main__':
    main()

