
def get_shortest_time(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    current_terrain = terrain[0]
    current_length = lengths[0]
    segment_index = 0

    # Loop through each segment
    while segment_index < n:
        # Check if Bob can fly over the current segment
        if current_terrain == "W" and stamina >= current_length:
            # Fly over the segment
            time += current_length
            stamina -= current_length
            segment_index += 1
            current_terrain = terrain[segment_index]
            current_length = lengths[segment_index]
        # Check if Bob can swim in the current segment
        elif current_terrain == "L" and stamina >= current_length:
            # Swim in the segment
            time += current_length
            stamina -= current_length
            segment_index += 1
            current_terrain = terrain[segment_index]
            current_length = lengths[segment_index]
        # Check if Bob can walk in the current segment
        elif current_terrain == "G" and stamina >= current_length:
            # Walk in the segment
            time += current_length
            stamina -= current_length
            segment_index += 1
            current_terrain = terrain[segment_index]
            current_length = lengths[segment_index]
        # Check if Bob needs to rest
        else:
            # Rest for one second
            time += 1
            stamina += 1

    # Return the shortest time
    return time

def main():
    n = int(input())
    lengths = list(map(int, input().split()))
    terrain = list(input())
    print(get_shortest_time(n, lengths, terrain))

if __name__ == '__main__':
    main()

