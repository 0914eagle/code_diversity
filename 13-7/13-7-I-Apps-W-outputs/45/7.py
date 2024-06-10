
def get_weight(w, h, u1, d1, u2, d2):
    # Initialize the weight of the snowball
    weight = w
    
    # Loop until the snowball reaches height 0
    while h > 0:
        # Increase the weight of the snowball by its current height
        weight += h
        
        # Check if the snowball hits either of the two stones
        if h == d1 or h == d2:
            # If the snowball hits the first stone, decrease its weight by the weight of the stone
            if h == d1:
                weight -= u1
            # If the snowball hits the second stone, decrease its weight by the weight of the stone
            else:
                weight -= u2
        
        # Move the snowball one meter down
        h -= 1
    
    # Return the final weight of the snowball
    return weight

def main():
    # Read the input
    w, h = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    
    # Call the get_weight function and print the result
    print(get_weight(w, h, u1, d1, u2, d2))

if __name__ == '__main__':
    main()

