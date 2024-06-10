
def get_wasted_paper(card_types, envelope_types):
    # Initialize variables
    wasted_paper = 0
    envelope_sizes = []

    # Sort the card types by width and height
    card_types.sort(key=lambda x: (x[0], x[1]))

    # Iterate through the card types
    for card_type in card_types:
        # Check if the envelope sizes are already sorted
        if len(envelope_sizes) == 0:
            envelope_sizes.append(card_type)
        else:
            # Check if the current card type fits in any of the existing envelope sizes
            for i in range(len(envelope_sizes)):
                if card_type[0] <= envelope_sizes[i][0] and card_type[1] <= envelope_sizes[i][1]:
                    break
            else:
                # If the card type doesn't fit in any of the existing envelope sizes, add a new envelope size
                envelope_sizes.append(card_type)

    # Calculate the wasted paper for each envelope size
    for envelope_size in envelope_sizes:
        wasted_paper += (envelope_size[0] * envelope_size[1]) - (card_type[0] * card_type[1])

    return wasted_paper

def main():
    card_types = []
    envelope_types = int(input())

    for i in range(envelope_types):
        card_types.append(list(map(int, input().split())))

    print(get_wasted_paper(card_types, envelope_types))

if __name__ == '__main__':
    main()

