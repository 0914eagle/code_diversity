
def get_shortest_time(segments, terrain, stamina):
    # Initialize variables
    time = 0
    current_segment = 0
    current_terrain = terrain[current_segment]
    current_stamina = stamina

    # Loop through each segment
    for i in range(len(segments)):
        # Check if Bob can move forward
        if current_stamina > 0:
            # Check if Bob can fly
            if current_terrain == "W" and current_stamina >= 2:
                time += 2
                current_stamina -= 2
            # Check if Bob can swim
            elif current_terrain == "L" and current_stamina >= 1:
                time += 3
                current_stamina -= 1
            # Check if Bob can walk
            elif current_terrain == "G" and current_stamina >= 1:
                time += 5
                current_stamina -= 1
            # Update current segment and terrain
            current_segment += 1
            current_terrain = terrain[current_segment]
        # Check if Bob needs to rest
        else:
            time += 1
            current_stamina = stamina

    return time

def main():
    segments = [int(x) for x in input().split()]
    terrain = input()
    stamina = int(input())
    print(get_shortest_time(segments, terrain, stamina))

if __name__ == '__main__':
    main()

