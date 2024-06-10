
def get_optimal_room_sizes(n, a, b):
    # Initialize the optimal room sizes as the current room sizes
    optimal_a, optimal_b = a, b
    # Initialize the minimum area as the current area
    min_area = a * b
    # Iterate over all possible combinations of increasing one side of the room
    for i in range(1, n + 1):
        # Calculate the area of the room with the current side increased by i meters
        area = (a + i) * (b + i)
        # If the area is less than or equal to the minimum area and the number of students is satisfied
        if area <= min_area and (area / i) >= 6:
            # Update the optimal room sizes and minimum area
            optimal_a, optimal_b = a + i, b + i
            min_area = area
    # Return the optimal room sizes
    return optimal_a, optimal_b

def main():
    n, a, b = map(int, input().split())
    optimal_a, optimal_b = get_optimal_room_sizes(n, a, b)
    print(optimal_a, optimal_b)

if __name__ == '__main__':
    main()

