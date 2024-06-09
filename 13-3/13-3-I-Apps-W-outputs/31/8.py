
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
    # Check if the grasshopper has visited the same position before
    if len(set(position)) != len(position):
        return "INFINITE"
    else:
        return "FINITE"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    directions = input()
    jumps = [int(x) for x in input().split()]
    print(f1(n, directions, jumps))

