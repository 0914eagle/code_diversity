
def solve(wall):
    # Initialize the minimum MP required to turn the wall into 1
    min_mp = 0
    # Loop through each row of the wall
    for i in range(len(wall)):
        # Loop through each column of the row
        for j in range(len(wall[i])):
            # If the current square contains a digit
            if wall[i][j] != -1:
                # Get the current digit
                digit = wall[i][j]
                # Get the cost of turning the digit into 1
                cost = costs[digit][1]
                # If the current digit is not 1
                if digit != 1:
                    # Get the cost of turning the digit into 0
                    cost0 = costs[digit][0]
                    # If the cost of turning the digit into 0 is less than the cost of turning it into 1
                    if cost0 < cost:
                        # Update the cost to the cost of turning the digit into 0
                        cost = cost0
                # Add the cost to the minimum MP required
                min_mp += cost
    # Return the minimum MP required
    return min_mp

def main():
    # Read the input
    h, w = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(10)]
    wall = [list(map(int, input().split())) for _ in range(h)]
    # Solve the problem
    min_mp = solve(wall)
    # Print the result
    print(min_mp)

if __name__ == '__main__':
    main()

