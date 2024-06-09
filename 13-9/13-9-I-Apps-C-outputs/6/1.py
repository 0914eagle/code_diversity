
def solve(rooms, beam_length):
    # Sort the rooms by their lower left corner (x1, y1)
    sorted_rooms = sorted(rooms, key=lambda x: (x[0], x[1]))

    # Initialize the maximum number of rooms hit to 0
    max_rooms_hit = 0

    # Loop through each room
    for i in range(len(sorted_rooms)):
        # Get the current room
        current_room = sorted_rooms[i]

        # Get the coordinates of the lower left corner and upper right corner of the current room
        x1, y1, x2, y2 = current_room

        # Find the intersection points of the current room with the line that represents the phaser beam
        intersection_points = get_intersection_points(x1, y1, x2, y2, beam_length)

        # If the current room is intersected by the phaser beam
        if intersection_points:
            # Increment the maximum number of rooms hit
            max_rooms_hit += 1

            # Find the coordinates of the intersection points
            x3, y3, x4, y4 = intersection_points

            # If the current room is not the last room
            if i != len(sorted_rooms) - 1:
                # Get the coordinates of the lower left corner and upper right corner of the next room
                x5, y5, x6, y6 = sorted_rooms[i + 1]

                # Find the intersection points of the next room with the line that represents the phaser beam
                next_intersection_points = get_intersection_points(x5, y5, x6, y6, beam_length)

                # If the next room is intersected by the phaser beam
                if next_intersection_points:
                    # Find the coordinates of the intersection points
                    x7, y7, x8, y8 = next_intersection_points

                    # If the intersection points of the current room and the next room are not the same
                    if (x3, y3, x4, y4) != (x7, y7, x8, y8):
                        # Increment the maximum number of rooms hit
                        max_rooms_hit += 1

    return max_rooms_hit

def get_intersection_points(x1, y1, x2, y2, beam_length):
    # Find the slope of the line that represents the phaser beam
    m = (y2 - y1) / (x2 - x1)

    # Find the intercept of the line that represents the phaser beam
    b = y1 - m * x1

    # Find the x-coordinate of the intersection point
    x_intersection = (beam_length * m + b) / (m ** 2 + 1)

    # Find the y-coordinate of the intersection point
    y_intersection = m * x_intersection + b

    # Return the coordinates of the intersection point
    return x_intersection, y_intersection

def main():
    rooms = []

    # Read the number of rooms and the length of the phaser beam from stdin
    r, beam_length = map(int, input().split())

    # Read the coordinates of the rooms from stdin
    for _ in range(r):
        x1, y1, x2, y2 = map(int, input().split())
        rooms.append((x1, y1, x2, y2))

    # Find the maximum number of rooms that can be hit by the phaser beam
    max_rooms_hit = solve(rooms, beam_length)

    # Print the maximum number of rooms that can be hit by the phaser beam
    print(max_rooms_hit)

if __name__ == "__main__":
    main()

