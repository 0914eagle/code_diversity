
def get_shortest_time(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    current_terrain = 0
    current_length = 0

    # Loop through each segment
    for i in range(n):
        # Check the terrain type
        if terrain[i] == "G":
            # Walking on grass is relaxing, gain 1 stamina
            stamina += 1
        elif terrain[i] == "W":
            # Swimming on water is relaxing, gain 1 stamina
            stamina += 1
        else:
            # Flying over lava is tiring, spend 1 stamina
            stamina -= 1

        # Check if stamina is negative
        if stamina < 0:
            # If stamina is negative, return -1 as the shortest time is not possible
            return -1

        # Check if the current segment is the last segment
        if i == n - 1:
            # If it is the last segment, return the current time
            return time

        # Check if the current segment is the first segment
        if i == 0:
            # If it is the first segment, set the current length to the length of the segment
            current_length = lengths[i]
        else:
            # If it is not the first segment, add the length of the current segment to the current length
            current_length += lengths[i]

        # Check if the current length is greater than the stamina
        if current_length > stamina:
            # If the current length is greater than the stamina, return -1 as the shortest time is not possible
            return -1

        # Check if the current terrain is water
        if terrain[i] == "W":
            # If the current terrain is water, add the time it takes to swim the current length to the time
            time += current_length * 3
        # Check if the current terrain is grass
        elif terrain[i] == "G":
            # If the current terrain is grass, add the time it takes to walk the current length to the time
            time += current_length * 5
        # Check if the current terrain is lava
        else:
            # If the current terrain is lava, add the time it takes to fly the current length to the time
            time += current_length * 1

        # Set the current length to 0
        current_length = 0

    # If the function reaches this point, return -1 as the shortest time is not possible
    return -1

def main():
    # Read the input
    n = int(input())
    lengths = list(map(int, input().split()))
    terrain = input()

    # Call the get_shortest_time function and print the result
    print(get_shortest_time(n, lengths, terrain))

if __name__ == '__main__':
    main()

