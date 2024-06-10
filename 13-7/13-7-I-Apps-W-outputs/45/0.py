
def find_final_weight(w, h, u1, d1, u2, d2):
    # Initialize the weight of the snowball
    weight = w
    # Initialize the current height of the snowball
    current_height = h
    # Initialize the weight of the stones
    stone_weight_1 = u1
    stone_weight_2 = u2
    # Initialize the height of the stones
    stone_height_1 = d1
    stone_height_2 = d2
    
    # Loop until the snowball reaches height 0
    while current_height > 0:
        # Increase the weight of the snowball by its current height
        weight += current_height
        # Check if the snowball hits either of the stones
        if current_height == stone_height_1 or current_height == stone_height_2:
            # If the snowball hits the first stone, decrease its weight by the weight of the stone
            if current_height == stone_height_1:
                weight -= stone_weight_1
            # If the snowball hits the second stone, decrease its weight by the weight of the stone
            if current_height == stone_height_2:
                weight -= stone_weight_2
            # If the snowball's weight becomes negative, set it to 0
            if weight < 0:
                weight = 0
        # Move the snowball one meter down
        current_height -= 1
    
    # Return the final weight of the snowball
    return weight

def main():
    # Read the input
    w, h, u1, d1, u2, d2 = map(int, input().split())
    # Find the final weight of the snowball
    final_weight = find_final_weight(w, h, u1, d1, u2, d2)
    # Print the final weight of the snowball
    print(final_weight)

if __name__ == '__main__':
    main()

