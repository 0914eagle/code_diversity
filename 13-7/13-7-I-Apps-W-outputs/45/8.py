
def get_snowball_weight(w, h, u1, d1, u2, d2):
    # Initialize the snowball's weight and height
    snowball_weight = w
    snowball_height = h
    
    # Loop until the snowball reaches height 0
    while snowball_height > 0:
        # Increase the snowball's weight by its current height
        snowball_weight += snowball_height
        
        # Check if the snowball hits either of the two stones
        if snowball_height == d1 or snowball_height == d2:
            # If the snowball hits the first stone, decrease its weight by the stone's weight
            if snowball_height == d1:
                snowball_weight -= u1
            # If the snowball hits the second stone, decrease its weight by the stone's weight
            elif snowball_height == d2:
                snowball_weight -= u2
        
        # Move the snowball one meter down
        snowball_height -= 1
    
    # Return the final weight of the snowball
    return snowball_weight

def main():
    # Read the input data
    w, h = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    
    # Calculate the final weight of the snowball
    snowball_weight = get_snowball_weight(w, h, u1, d1, u2, d2)
    
    # Print the final weight of the snowball
    print(snowball_weight)

if __name__ == '__main__':
    main()

