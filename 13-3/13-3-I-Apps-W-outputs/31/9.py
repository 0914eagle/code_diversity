
def f1(n, directions, distances):
    # Initialize a list to store the position of the grasshopper
    position = [0]
    # Loop through the directions and distances
    for i in range(n):
        # If the direction is ">", move the grasshopper to the right
        if directions[i] == ">":
            position.append(position[i] + distances[i])
        # If the direction is "<", move the grasshopper to the left
        else:
            position.append(position[i] - distances[i])
    # Check if the grasshopper has jumped out of the strip
    if position[-1] < 0 or position[-1] >= n:
        return "INFINITE"
    # If the grasshopper has not jumped out of the strip, return "FINITE"
    return "FINITE"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    directions = input()
    distances = [int(x) for x in input().split()]
    print(f1(n, directions, distances))

