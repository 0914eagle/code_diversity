
def get_optimal_room_size(n, a, b):
    # Initialize the optimal room size as the current room size
    optimal_room_size = (a, b)
    
    # Loop through all possible combinations of enlarging either the width or the length of the room
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the new room size by enlarging either the width or the length by i or j meters, whichever is smaller
            new_room_size = (a + min(i, j), b + min(i, j))
            
            # If the new room size is valid and has a smaller area than the current optimal room size, update the optimal room size
            if new_room_size[0] * new_room_size[1] <= 6 * n and new_room_size[0] * new_room_size[1] < optimal_room_size[0] * optimal_room_size[1]:
                optimal_room_size = new_room_size
    
    return optimal_room_size

def main():
    n, a, b = map(int, input().split())
    optimal_room_size = get_optimal_room_size(n, a, b)
    print(optimal_room_size[0] * optimal_room_size[1])
    print(optimal_room_size[0], optimal_room_size[1])

if __name__ == '__main__':
    main()

