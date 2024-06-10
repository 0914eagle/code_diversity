
def get_minimum_area(n, a, b):
    # Calculate the minimum area required for the room
    min_area = 6 * n
    
    # Initialize the sides of the room as the given values
    a_1 = a
    b_1 = b
    
    # If the total area of the room is less than the minimum area, increase the side with the smaller area until the total area is equal to the minimum area
    if a_1 * b_1 < min_area:
        if a_1 < b_1:
            a_1 = min_area // b_1
        else:
            b_1 = min_area // a_1
    
    # Return the final area of the room and its sizes
    return min_area, a_1, b_1

def main():
    n, a, b = map(int, input().split())
    min_area, a_1, b_1 = get_minimum_area(n, a, b)
    print(min_area)
    print(a_1, b_1)

if __name__ == '__main__':
    main()

