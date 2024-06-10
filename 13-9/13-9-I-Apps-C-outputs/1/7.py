
def get_waste_paper(card_types, envelope_sizes):
    # Initialize variables
    waste_paper = 0
    
    # Iterate through each card type
    for card_type in card_types:
        # Get the width and height of the card
        width, height = card_type[0], card_type[1]
        
        # Find the smallest envelope size that fits the card
        envelope_size = get_smallest_envelope_size(width, height, envelope_sizes)
        
        # Calculate the waste paper for this card
        waste_paper += calculate_waste_paper(width, height, envelope_size)
    
    return waste_paper

def get_smallest_envelope_size(width, height, envelope_sizes):
    # Initialize variables
    smallest_envelope_size = (0, 0)
    smallest_waste_paper = float('inf')
    
    # Iterate through each envelope size
    for envelope_size in envelope_sizes:
        # Get the width and height of the envelope
        envelope_width, envelope_height = envelope_size[0], envelope_size[1]
        
        # Calculate the waste paper for this envelope size
        waste_paper = calculate_waste_paper(width, height, envelope_size)
        
        # Check if this envelope size is the smallest so far
        if waste_paper < smallest_waste_paper:
            smallest_waste_paper = waste_paper
            smallest_envelope_size = envelope_size
    
    return smallest_envelope_size

def calculate_waste_paper(width, height, envelope_size):
    # Get the width and height of the envelope
    envelope_width, envelope_height = envelope_size[0], envelope_size[1]
    
    # Calculate the area of the card
    card_area = width * height
    
    # Calculate the area of the envelope
    envelope_area = envelope_width * envelope_height
    
    # Calculate the waste paper
    waste_paper = envelope_area - card_area
    
    return waste_paper

def main():
    # Read the input
    card_types = []
    for _ in range(int(input())):
        card_types.append(tuple(map(int, input().split())))
    envelope_sizes = []
    for _ in range(int(input())):
        envelope_sizes.append(tuple(map(int, input().split())))
    
    # Calculate the waste paper
    waste_paper = get_waste_paper(card_types, envelope_sizes)
    
    # Print the output
    print(waste_paper)

if __name__ == '__main__':
    main()

