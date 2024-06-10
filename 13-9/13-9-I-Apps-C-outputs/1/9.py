
def get_envelope_sizes(card_types):
    # Find the smallest common multiple of the card widths and heights
    lcm_wh = _get_lcm(list(map(lambda x: x[0] * x[1], card_types)))
    
    # Create a list of envelope sizes that are multiples of the lcm
    envelope_sizes = [(lcm_wh // x, lcm_wh // x) for x in range(1, lcm_wh + 1) if lcm_wh % x == 0]
    
    # Return the list of envelope sizes
    return envelope_sizes

def get_wasted_paper(card_types, envelope_sizes):
    # Initialize the total wasted paper to 0
    total_wasted_paper = 0
    
    # Iterate over the card types
    for card_type in card_types:
        # Find the envelope size that is closest to the card size
        envelope_size = min(envelope_sizes, key=lambda x: abs(x[0] * x[1] - card_type[0] * card_type[1]))
        
        # Calculate the wasted paper for this card type
        wasted_paper = (envelope_size[0] * envelope_size[1]) - (card_type[0] * card_type[1])
        
        # Add the wasted paper to the total wasted paper
        total_wasted_paper += wasted_paper * card_type[2]
    
    # Return the total wasted paper
    return total_wasted_paper

def _get_lcm(numbers):
    # Find the least common multiple of a list of numbers
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = _lcm(lcm, num)
    return lcm

def _lcm(a, b):
    # Find the least common multiple of two numbers
    return a * b // _gcd(a, b)

def _gcd(a, b):
    # Find the greatest common divisor of two numbers
    if b == 0:
        return a
    return _gcd(b, a % b)

if __name__ == '__main__':
    card_types = [(10, 10, 5), (9, 8, 10), (4, 12, 20), (12, 4, 8), (2, 3, 16)]
    envelope_sizes = get_envelope_sizes(card_types)
    print(get_wasted_paper(card_types, envelope_sizes))

