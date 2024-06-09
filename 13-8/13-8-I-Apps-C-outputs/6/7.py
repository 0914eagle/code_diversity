
def divide_swimmers(n, positions):
    # Sort the positions of the swimmers by their x-coordinate
    sorted_positions = sorted(positions, key=lambda x: x[0])

    # Initialize the locations of the lifeguards
    guard1_x = 0
    guard2_x = 0

    # Divide the swimmers into two groups
    group1 = []
    group2 = []
    for i in range(n):
        if i % 2 == 0:
            group1.append(sorted_positions[i])
        else:
            group2.append(sorted_positions[i])

    # Find the location of the second lifeguard
    guard2_x = guard1_x + (group2[-1][0] - group1[-1][0])

    return guard1_x, guard2_x

