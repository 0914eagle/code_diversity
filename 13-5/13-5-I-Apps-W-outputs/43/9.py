
def get_input():
    N = int(input())
    stones = input()
    return N, stones

def f1(N, stones):
    # Initialize the number of operations to 0
    operations = 0
    
    # Loop through the stones from left to right
    for i in range(N):
        # If the current stone is white and the next stone is red, swap them
        if stones[i] == "W" and stones[i+1] == "R":
            operations += 1
            stones = stones[:i] + "R" + stones[i+1:]
    
    return operations

def f2(N, stones):
    # Initialize the number of operations to 0
    operations = 0
    
    # Loop through the stones from left to right
    for i in range(N):
        # If the current stone is white, change its color to red
        if stones[i] == "W":
            operations += 1
            stones = stones[:i] + "R" + stones[i+1:]
    
    return operations

def main():
    N, stones = get_input()
    print(min(f1(N, stones), f2(N, stones)))

if __name__ == '__main__':
    main()

