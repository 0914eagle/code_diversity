
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

        # Check if the current segment is water or lava
        if current_terrain == "W":
            # Swim in the water
            time += 3 * length
            current_stamina += length
        elif current_terrain == "L":
            # Fly over the lava
            time += 1 * length
            current_stamina -= length
        else:
            # Walk on the grass
            time += 5 * length
            current_stamina += length

        # Update the position and terrain
        position += length
        current_terrain = terrain[i % len(terrain)]

        # Check if the current stamina is negative
        if current_stamina < 0:
            return -1

    # Return the shortest time
    return time

def main():
    n = int(input())
    lengths = list(map(int, input().split()))
    terrain = input()
    stamina = 0
    print(get_shortest_time(n, lengths, terrain, stamina))

if __name__ == '__main__':
    main()

