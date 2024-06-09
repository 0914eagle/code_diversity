
def get_terrain_type(segment_length, terrain_type):
    if terrain_type == "G":
        return "Grass"
    elif terrain_type == "W":
        return "Water"
    else:
        return "Lava"

def get_movement_time(segment_length, movement_type):
    if movement_type == "F":
        return segment_length
    elif movement_type == "S":
        return segment_length * 3
    else:
        return segment_length * 5

def get_stamina_gain(segment_length, movement_type):
    if movement_type == "F":
        return -segment_length
    else:
        return segment_length

def solve(n, segment_lengths, terrain_types):
    # Initialize the variables
    time = 0
    stamina = 0
    movement_type = "W"
    segment_index = 0

    # Loop through the segments
    while segment_index < n:
        # Get the current segment information
        segment_length = segment_lengths[segment_index]
        terrain_type = get_terrain_type(segment_length, terrain_types[segment_index])

        # Check if the current segment is lava and the stamina is not enough
        if terrain_type == "Lava" and stamina < 2:
            # Switch to swimming
            movement_type = "S"

        # Get the movement time and stamina gain for the current segment
        movement_time = get_movement_time(segment_length, movement_type)
        stamina_gain = get_stamina_gain(segment_length, movement_type)

        # Update the variables
        time += movement_time
        stamina += stamina_gain
        segment_index += 1

    # Return the final time
    return time

if __name__ == '__main__':
    n = int(input())
    segment_lengths = list(map(int, input().split()))
    terrain_types = list(input())
    print(solve(n, segment_lengths, terrain_types))

