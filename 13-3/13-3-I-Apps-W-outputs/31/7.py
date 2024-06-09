
def f1(n, directions, lengths):
    # Initialize a list to store the position of the grasshopper
    position = [0]
    # Loop through the directions and lengths
    for i in range(n):
        # If the direction is ">", move the grasshopper to the right
        if directions[i] == ">":
            position.append(position[i] + lengths[i])
        # If the direction is "<", move the grasshopper to the left
        else:
            position.append(position[i] - lengths[i])
    # If the grasshopper ever jumps out of the strip, return "INFINITE"
    if max(position) > n or min(position) < 0:
        return "INFINITE"
    # Otherwise, return "FINITE"
    else:
        return "FINITE"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    directions = input()
    lengths = [int(x) for x in input().split()]
    print(f1(n, directions, lengths))

