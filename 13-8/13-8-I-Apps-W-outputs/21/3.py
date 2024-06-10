
def get_optimal_room_size(n, a, b):
    # Initialize the optimal room size as (a, b)
    optimal_room_size = (a, b)
    
    # Loop through all possible combinations of enlarging the sides of the room
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the total area of the room with the current side lengths
            total_area = a * b
            
            # Calculate the area per student for the current side lengths
            area_per_student = total_area / n
            
            # Check if the area per student is greater than or equal to 6 square meters
            if area_per_student >= 6:
                # If the area per student is greater than or equal to 6 square meters, update the optimal room size
                optimal_room_size = (a + i, b + j)
    
    return optimal_room_size

def main():
    n, a, b = map(int, input().split())
    optimal_room_size = get_optimal_room_size(n, a, b)
    print(optimal_room_size[0] * optimal_room_size[1])
    print(optimal_room_size[0], optimal_room_size[1])

if __name__ == '__main__':
    main()

