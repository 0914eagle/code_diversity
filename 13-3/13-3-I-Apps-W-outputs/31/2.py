
def f1(n, directions, lengths):
    # Initialize a list to store the positions of the grasshopper
    positions = [0]
    # Iterate through the directions and lengths
    for i in range(n):
        # If the direction is ">", move right by the length
        if directions[i] == ">":
            positions.append(positions[-1] + lengths[i])
        # If the direction is "<", move left by the length
        else:
            positions.append(positions[-1] - lengths[i])
    # If the grasshopper has visited a position before, it will continue to jump forever
    if len(set(positions)) != len(positions):
        return "INFINITE"
    # If the grasshopper has not visited a position before, it will eventually jump out of the strip
    else:
        return "FINITE"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    directions = input()
    lengths = [int(x) for x in input().split()]
    print(f1(n, directions, lengths))

