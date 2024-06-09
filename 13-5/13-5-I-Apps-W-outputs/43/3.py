
def get_input():
    N = int(input())
    stones = input()
    return N, stones

def f1(N, stones):
    # Initialize variables
    red_stones = 0
    white_stones = 0
    operations = 0

    # Iterate through the stones
    for i in range(N):
        if stones[i] == "R":
            red_stones += 1
        else:
            white_stones += 1

        # Check if a white stone is placed to the immediate left of a red stone
        if i > 0 and stones[i-1] == "R" and stones[i] == "W":
            operations += 1

    return operations

def f2(N, stones):
    # Initialize variables
    red_stones = 0
    white_stones = 0
    operations = 0

    # Iterate through the stones
    for i in range(N):
        if stones[i] == "R":
            red_stones += 1
        else:
            white_stones += 1

        # Check if a white stone is placed to the immediate left of a red stone
        if i > 0 and stones[i-1] == "R" and stones[i] == "W":
            operations += 1

    # If there are no white stones placed to the immediate left of red stones, return 0
    if operations == 0:
        return 0

    # Otherwise, find the minimum number of operations needed to move all the white stones to the end of the row
    while white_stones > 0:
        # Find the first white stone
        for i in range(N):
            if stones[i] == "W":
                break

        # Move the first white stone to the end of the row
        stones = stones[:i] + stones[i+1:] + "W"
        white_stones -= 1
        operations += 1

    return operations

if __name__ == '__main__':
    N, stones = get_input()
    print(f1(N, stones))
    print(f2(N, stones))

