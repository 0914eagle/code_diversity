
def get_min_mp(costs, wall):
    # Initialize a dictionary to store the minimum MP required to turn each digit into 1
    min_mp = {digit: float('inf') for digit in range(10)}
    min_mp[1] = 0

    # Loop through each row of the wall
    for i in range(len(wall)):
        # Loop through each column of the row
        for j in range(len(wall[i])):
            # If the current square contains a digit, update the minimum MP required to turn it into 1
            if wall[i][j] != -1:
                min_mp[wall[i][j]] = min(min_mp[wall[i][j]], min_mp[1] + costs[wall[i][j]][1])

    # Return the minimum total MP required to turn every digit on the wall into 1
    return sum(min_mp.values())

def main():
    # Read the input data
    H, W = map(int, input().split())
    costs = [[int(x) for x in input().split()] for _ in range(10)]
    wall = [list(map(int, input().split())) for _ in range(H)]

    # Solve the problem
    min_mp = get_min_mp(costs, wall)

    # Print the minimum total MP required to turn every digit on the wall into 1
    print(min_mp)

if __name__ == '__main__':
    main()

