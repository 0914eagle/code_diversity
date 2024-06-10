
def get_snowball_weight(h, w, u1, d1, u2, d2):
    # Initialize the snowball's weight
    weight = w
    
    # Loop through each second
    for i in range(h):
        # Increase the snowball's weight by its current height
        weight += i
        
        # Check if the snowball hits either of the stones
        if weight >= u1 and d1 == i+1:
            # If it hits the first stone, decrease its weight by the stone's weight
            weight -= u1
        if weight >= u2 and d2 == i+1:
            # If it hits the second stone, decrease its weight by the stone's weight
            weight -= u2
        
        # If the snowball's weight becomes negative, set it to zero
        if weight < 0:
            weight = 0
    
    # Return the final weight of the snowball
    return weight

def main():
    # Read input from stdin
    h, w = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    
    # Call the get_snowball_weight function and print the result
    print(get_snowball_weight(h, w, u1, d1, u2, d2))

if __name__ == '__main__':
    main()

