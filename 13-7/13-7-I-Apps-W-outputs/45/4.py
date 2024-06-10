
def get_snowball_weight(w, h, u1, d1, u2, d2):
    # Initialize the snowball's weight and height
    snowball_weight = w
    snowball_height = h
    
    # Loop until the snowball reaches height 0
    while snowball_height > 0:
        # Increase the snowball's weight by its current height
        snowball_weight += snowball_height
        
        # Check if the snowball hits either stone
        if snowball_height == d1 or snowball_height == d2:
            # If the snowball hits the first stone, decrease its weight by the stone's weight
            if snowball_height == d1:
                snowball_weight -= u1
            # If the snowball hits the second stone, decrease its weight by the stone's weight
            elif snowball_height == d2:
                snowball_weight -= u2
            
            # If the snowball's weight becomes negative, set it to 0
            if snowball_weight < 0:
                snowball_weight = 0
        
        # Move the snowball one meter down
        snowball_height -= 1
    
    # Return the final weight of the snowball
    return snowball_weight

def main():
    # Read the input data
    w, h = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    
    # Call the get_snowball_weight function and print the result
    print(get_snowball_weight(w, h, u1, d1, u2, d2))

if __name__ == '__main__':
    main()

