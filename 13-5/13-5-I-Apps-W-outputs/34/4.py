
def get_shortest_time(n, lengths, terrain, stamina):
    # Initialize variables
    time = 0
    position = 0
    current_terrain = terrain[0]
    current_stamina = stamina

    # Iterate through the segments
    for i in range(n):
        # Check if Bob can move to the next segment
        if current_terrain == "G" and current_stamina > 0:
            # Walking is relaxing, so Bob gains stamina
            current_stamina += 1
        elif current_terrain == "W" and current_stamina > 1:
            # Swimming is relaxing, so Bob gains stamina
            current_stamina += 1
        elif current_terrain == "L" and current_stamina > 2:
            # Flying is tiring, so Bob spends stamina
            current_stamina -= 2

        # Move to the next segment
        position += lengths[i]
        time += get_time(current_terrain, lengths[i])
        current_terrain = terrain[i]

    return time

def get_time(terrain, length):
    if terrain == "G":
        return length * 5
    elif terrain == "W":
        return length * 3
    else:
        return length * 1

if __name__ == '__main__':
    n = int(input())
    lengths = list(map(int, input().split()))
    terrain = input()
    stamina = 0
    print(get_shortest_time(n, lengths, terrain, stamina))

