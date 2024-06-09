
def is_wall_completable(height, width, bricks):
    # Initialize a list to store the bricks
    brick_list = []

    # Iterate through the bricks and add them to the list
    for brick in bricks:
        brick_list.append(brick)

    # Initialize a variable to store the total width of the wall
    total_width = 0

    # Iterate through the bricks and check if the total width is greater than the width of the wall
    for brick in brick_list:
        total_width += brick
        if total_width > width:
            return "NO"

    # Check if the total height of the wall is greater than the height of the wall
    if len(brick_list) * height > height:
        return "NO"

    # If the wall is completable, return "YES"
    return "YES"

