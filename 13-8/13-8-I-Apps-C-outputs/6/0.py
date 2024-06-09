
def solve(n, positions):
    # Sort the positions of the swimmers by their x-coordinate
    sorted_positions = sorted(positions, key=lambda x: x[0])

    # Initialize the positions of you and your coworker
    you = [0, 0]
    coworker = [0, 0]

    # Divide the swimmers into two groups
    group1 = []
    group2 = []
    for i in range(n):
        if i % 2 == 0:
            group1.append(sorted_positions[i])
        else:
            group2.append(sorted_positions[i])

    # Find the position of you and your coworker that minimizes the total distance to the swimmers
    min_distance = float('inf')
    for i in range(n):
        for j in range(n):
            distance = abs(you[0] - group1[i][0]) + abs(you[1] - group1[i][1]) + abs(coworker[0] - group2[j][0]) + abs(coworker[1] - group2[j][1])
            if distance < min_distance:
                min_distance = distance
                you = group1[i]
                coworker = group2[j]

    return [you, coworker]

