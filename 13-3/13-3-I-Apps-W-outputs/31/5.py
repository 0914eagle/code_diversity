
def f1(n, directions, jumps):
    # Initialize a list to store the position of the grasshopper
    position = [0]
    # Iterate through the directions and jumps
    for i in range(n):
        # If the direction is ">", move right
        if directions[i] == ">":
            position.append(position[i] + jumps[i])
        # If the direction is "<", move left
        else:
            position.append(position[i] - jumps[i])
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
    jumps = list(map(int, input().split()))
    print(f1(n, directions, jumps))

