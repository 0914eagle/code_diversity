
def get_shortest_time(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    segment = 0
    current_terrain = terrain[segment]

    # Loop through each segment
    while segment < n:
        # Get the length of the current segment
        length = lengths[segment]

        # Check if the current segment is grass or water
        if current_terrain == "G" or current_terrain == "W":
            # Walk or swim the length of the segment
            time += length * 5
            stamina += length

        # Check if the current segment is lava
        elif current_terrain == "L":
            # Spend stamina for flying over the lava
            stamina -= length
            time += length * 1

        # Update the current terrain and segment
        segment += 1
        if segment < n:
            current_terrain = terrain[segment]

    # Return the shortest time
    return time

def main():
    n = int(input())
    lengths = list(map(int, input().split()))
    terrain = input()
    print(get_shortest_time(n, lengths, terrain))

if __name__ == '__main__':
    main()

