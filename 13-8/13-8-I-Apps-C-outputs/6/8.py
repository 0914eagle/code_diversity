
def solve(n, positions):
    # Sort the positions of the swimmers by their x-coordinate
    positions.sort(key=lambda x: x[0])

    # Initialize the positions of the lifeguards
    guard1_x = 0
    guard1_y = 0
    guard2_x = 0
    guard2_y = 0

    # Divide the swimmers into two groups
    group1 = []
    group2 = []
    for i in range(n):
        if i % 2 == 0:
            group1.append(positions[i])
        else:
            group2.append(positions[i])

    # Find the optimal position for the first lifeguard
    guard1_x = group1[0][0]
    guard1_y = group1[0][1]

    # Find the optimal position for the second lifeguard
    guard2_x = group2[0][0]
    guard2_y = group2[0][1]

    return [guard1_x, guard1_y], [guard2_x, guard2_y]

