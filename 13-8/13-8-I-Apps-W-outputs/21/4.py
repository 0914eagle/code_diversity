
def get_optimal_room_size(n, a, b):
    # Initialize the optimal room size as (a, b)
    optimal_room_size = (a, b)
    
    # Loop through all possible combinations of enlarging either side of the room
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the total area of the room with the current combination of sizes
            total_area = (a + i) * (b + j)
            
            # Check if the total area is greater than or equal to 6n and less than or equal to the current optimal room size
            if total_area >= 6 * n and total_area <= optimal_room_size[0] * optimal_room_size[1]:
                # Update the optimal room size
                optimal_room_size = (a + i, b + j)
    
    return optimal_room_size

def main():
    n, a, b = map(int, input().split())
    print(*get_optimal_room_size(n, a, b))

if __name__ == '__main__':
    main()

