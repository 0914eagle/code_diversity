
def solve(H, W, C, A):
    # Initialize the minimum MP required to turn every digit on the wall into 1
    min_mp = 0
    # Initialize the number of digits on the wall
    num_digits = 0
    # Initialize the number of digits that have been turned into 1
    num_turned = 0
    # Initialize the cost of turning a digit into 1
    turn_cost = 0
    # Initialize the cost of turning a digit into another digit
    turn_into_cost = 0

    # Loop through each row of the wall
    for i in range(H):
        # Loop through each column of the wall
        for j in range(W):
            # If the current square contains a digit
            if A[i][j] != -1:
                # Increment the number of digits on the wall
                num_digits += 1
                # If the current digit is not 1
                if A[i][j] != 1:
                    # Increment the minimum MP required to turn every digit on the wall into 1
                    min_mp += C[A[i][j] - 1][1]
                # If the current digit is 1
                else:
                    # Increment the number of digits that have been turned into 1
                    num_turned += 1

    # If not all digits have been turned into 1
    if num_turned < num_digits:
        # Initialize the cost of turning a digit into 1
        turn_cost = min_mp // num_digits
        # Initialize the cost of turning a digit into another digit
        turn_into_cost = min_mp % num_digits

        # Loop through each row of the wall
        for i in range(H):
            # Loop through each column of the wall
            for j in range(W):
                # If the current square contains a digit
                if A[i][j] != -1:
                    # If the current digit is not 1
                    if A[i][j] != 1:
                        # Turn the current digit into 1
                        A[i][j] = 1
                        # Increment the number of digits that have been turned into 1
                        num_turned += 1
                        # Decrement the minimum MP required to turn every digit on the wall into 1
                        min_mp -= C[A[i][j] - 1][1]
                    # If the current digit is 1
                    else:
                        # If the cost of turning a digit into 1 is not equal to the cost of turning a digit into another digit
                        if turn_cost != turn_into_cost:
                            # Turn the current digit into another digit
                            A[i][j] = (A[i][j] + 1) % 10
                            # Increment the minimum MP required to turn every digit on the wall into 1
                            min_mp += turn_into_cost
                        # If the cost of turning a digit into 1 is equal to the cost of turning a digit into another digit
                        else:
                            # Turn the current digit into another digit
                            A[i][j] = (A[i][j] + 1) % 10
                            # Increment the minimum MP required to turn every digit on the wall into 1
                            min_mp += turn_cost

    # Return the minimum total amount of MP required to turn every digit on the wall into 1
    return min_mp

def main():
    # Read the input
    H, W = map(int, input().split())
    C = []
    for i in range(10):
        C.append(list(map(int, input().split())))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    # Solve the problem
    result = solve(H, W, C, A)

    # Print the output
    print(result)

if __name__ == '__main__':
    main()

