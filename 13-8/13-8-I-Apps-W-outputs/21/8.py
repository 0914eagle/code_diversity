
def get_optimal_room_size(n, a, b):
    # Initialize optimal room size as (a, b)
    optimal_room_size = (a, b)
    
    # Loop through all possible combinations of increasing a or b by 1 meter
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Calculate the total area of the room with sides a+i and b+j
            total_area = (a+i) * (b+j)
            
            # If the total area is less than or equal to 6n and greater than the current optimal room size, update the optimal room size
            if total_area <= 6*n and total_area > optimal_room_size[0] * optimal_room_size[1]:
                optimal_room_size = (a+i, b+j)
    
    return optimal_room_size

def main():
    n, a, b = map(int, input().split())
    optimal_room_size = get_optimal_room_size(n, a, b)
    print(optimal_room_size[0] * optimal_room_size[1])
    print(optimal_room_size[0], optimal_room_size[1])

if __name__ == '__main__':
    main()

