
def get_optimal_room_size(n, a, b):
    # Initialize the optimal room size as (a, b)
    optimal_room_size = (a, b)
    
    # Loop through all possible combinations of (a, b)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the total area of the current room
            current_room_area = i * a + j * b
            
            # Check if the current room area is greater than or equal to 6n and smaller than or equal to the optimal room area
            if 6 * n <= current_room_area <= optimal_room_size[0] * optimal_room_size[1]:
                # Update the optimal room size if the current room area is smaller than the optimal room area
                optimal_room_size = (i, j)
    
    return optimal_room_size

def main():
    n, a, b = map(int, input().split())
    optimal_room_size = get_optimal_room_size(n, a, b)
    print(optimal_room_size[0] * optimal_room_size[1])
    print(optimal_room_size[0], optimal_room_size[1])

if __name__ == '__main__':
    main()

