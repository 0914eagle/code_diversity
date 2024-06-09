
def get_input():
    N = int(input())
    stones = input()
    return N, stones

def f1(N, stones):
    # Initialize variables
    count = 0
    i = 0
    j = 1
    while i < N - 1:
        # If the current stone is red and the next stone is white, swap them
        if stones[i] == "R" and stones[j] == "W":
            count += 1
            stones = stones[:i] + "W" + stones[i+1:j] + "R" + stones[j+1:]
            i += 1
            j += 1
        # If the current stone is white and the next stone is red, change the color of the current stone to red
        elif stones[i] == "W" and stones[j] == "R":
            count += 1
            stones = stones[:i] + "R" + stones[i+1:]
        i += 1
        j += 1
    return count

def f2(N, stones):
    # Initialize variables
    count = 0
    i = 0
    while i < N - 1:
        # If the current stone is white and the next stone is red, swap them
        if stones[i] == "W" and stones[i+1] == "R":
            count += 1
            stones = stones[:i] + "R" + stones[i+1:] + "W" + stones[i+2:]
            i += 1
        i += 1
    return count

if __name__ == '__main__':
    N, stones = get_input()
    print(min(f1(N, stones), f2(N, stones)))

