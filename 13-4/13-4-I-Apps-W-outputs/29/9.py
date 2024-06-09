
import sys

def get_inconvenience(bridges, m):
    # Initialize a dictionary to store the inconvenience for each bridge
    inconvenience = {i: 0 for i in range(1, m + 1)}

    # Iterate through the bridges and calculate the inconvenience after each bridge collapses
    for i in range(1, m):
        # Get the indices of the islands connected by the current bridge
        island1, island2 = bridges[i]

        # Iterate through the remaining bridges and check if they connect the same two islands
        for j in range(i + 1, m):
            # If the current bridge connects the same two islands as the next bridge, increase the inconvenience
            if bridges[j][0] == island1 and bridges[j][1] == island2:
                inconvenience[i + 1] += 1
            elif bridges[j][0] == island2 and bridges[j][1] == island1:
                inconvenience[i + 1] += 1

    return inconvenience

n, m = map(int, input().split())
bridges = []
for _ in range(m):
    a, b = map(int, input().split())
    bridges.append((a, b))

inconvenience = get_inconvenience(bridges, m)
for i in range(1, m + 1):
    print(inconvenience[i])

