
def f1(N, stones):
    # Initialize the number of operations to 0
    operations = 0
    # Loop through the stones from left to right
    for i in range(N):
        # If the current stone is white and the next stone is red, swap them
        if stones[i] == "W" and stones[i+1] == "R":
            operations += 1
            stones[i], stones[i+1] = stones[i+1], stones[i]
    return operations

def f2(N, stones):
    # Initialize the number of operations to 0
    operations = 0
    # Loop through the stones from left to right
    for i in range(N):
        # If the current stone is white, change its color to red
        if stones[i] == "W":
            operations += 1
            stones[i] = "R"
    return operations

if __name__ == '__main__':
    N = int(input())
    stones = list(input())
    print(min(f1(N, stones), f2(N, stones)))

