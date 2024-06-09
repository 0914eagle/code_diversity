
def f1(n, directions, lengths):
    # Initialize a list to store the position of the grasshopper
    position = [0]
    # Loop through the directions and lengths
    for i in range(n):
        # If the direction is ">", move right by the length
        if directions[i] == ">":
            position.append(position[i] + lengths[i])
        # If the direction is "<", move left by the length
        else:
            position.append(position[i] - lengths[i])
    # If the grasshopper ever reaches the end of the strip, return "FINITE"
    if position[-1] == n:
        return "FINITE"
    # If the grasshopper ever reaches the beginning of the strip, return "INFINITE"
    elif position[-1] == 0:
        return "INFINITE"
    # If the grasshopper never reaches the end of the strip, return "INFINITE"
    else:
        return "INFINITE"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    directions = input()
    lengths = [int(x) for x in input().split()]
    print(f1(n, directions, lengths))

