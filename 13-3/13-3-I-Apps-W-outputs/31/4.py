
def f1(n, directions, distances):
    # Initialize a list to store the position of the grasshopper
    position = [0]
    # Loop through the directions and distances
    for i in range(n):
        # If the direction is ">", move the grasshopper to the right by the distance
        if directions[i] == ">":
            position.append(position[i] + distances[i])
        # If the direction is "<", move the grasshopper to the left by the distance
        else:
            position.append(position[i] - distances[i])
    # If the grasshopper ever jumps out of the strip, return "INFINITE"
    if max(position) > n or min(position) < 0:
        return "INFINITE"
    # Otherwise, return "FINITE"
    return "FINITE"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    directions = input()
    distances = [int(x) for x in input().split()]
    print(f1(n, directions, distances))

