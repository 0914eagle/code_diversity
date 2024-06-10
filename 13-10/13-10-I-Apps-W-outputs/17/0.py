
def get_min_distance(n, k, rooms):
    # Initialize variables
    min_distance = float('inf')
    start_index = 0
    end_index = 0

    # Iterate through the string of rooms
    for i in range(n):
        # If the current room is occupied, skip it
        if rooms[i] == '1':
            continue
        # If the current room is free, check if it is the start of a sequence of k + 1 free rooms
        if i - start_index + 1 == k + 1:
            # If it is, calculate the distance between the current room and the farthest occupied room before it
            distance = i - end_index
            # If the distance is less than the current minimum distance, update the minimum distance and the indices of the start and end of the sequence
            if distance < min_distance:
                min_distance = distance
                start_index = i - k
                end_index = i

    # Return the minimum distance and the indices of the start and end of the sequence
    return min_distance, start_index, end_index

def main():
    # Read the input
    n, k = map(int, input().split())
    rooms = input()

    # Call the function to get the minimum distance and the indices of the start and end of the sequence
    min_distance, start_index, end_index = get_min_distance(n, k, rooms)

    # Print the minimum distance
    print(min_distance)

if __name__ == '__main__':
    main()

