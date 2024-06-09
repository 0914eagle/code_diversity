
def get_shortest_time(n, lengths, terrain, stamina):
    # Initialize variables
    time = 0
    position = 0
    current_terrain = terrain[0]
    current_stamina = stamina

    # Iterate through the segments
    for i in range(n):
        # Get the length of the current segment
        length = lengths[i]

        # Check if the current segment is grass or water
        if current_terrain == "G" or current_terrain == "W":
            # Walk or swim to the next segment
            time += length * 5
            position += length
            current_stamina += length

        # Check if the current segment is lava
        elif current_terrain == "L":
            # Check if the current stamina is enough to fly over the lava
            if current_stamina >= length:
                # Fly over the lava
                time += length * 1
                position += length
                current_stamina -= length
            else:
                # Walk or swim to the next segment
                time += length * 5
                position += length
                current_stamina += length - length

        # Update the current terrain and stamina
        current_terrain = terrain[i + 1]
        current_stamina = max(current_stamina, 0)

    # Return the shortest time to reach the nest
    return time

def main():
    # Read the input
    n = int(input())
    lengths = list(map(int, input().split()))
    terrain = input()
    stamina = 0

    # Call the function to get the shortest time
    time = get_shortest_time(n, lengths, terrain, stamina)

    # Print the output
    print(time)

if __name__ == '__main__':
    main()

