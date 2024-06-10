
def solve(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Loop through all the planks
    for i in range(10**100):
        # Check if the current plank is divisible by r
        if i % r == 0:
            # If it is, paint it red
            painted_planks.append("R")
        # Check if the current plank is divisible by b
        elif i % b == 0:
            # If it is, paint it blue
            painted_planks.append("B")
        # If the current plank is not divisible by either r or b, don't paint it

    # Loop through the painted planks and check for consecutive planks with the same color
    for i in range(len(painted_planks) - k + 1):
        # Check if the current plank and the next k-1 planks have the same color
        if all(painted_planks[i + j] == painted_planks[i] for j in range(k)):
            # If they do, return "REBEL"
            return "REBEL"

    # If no consecutive planks with the same color are found, return "OBEY"
    return "OBEY"

def main():
    # Read the number of test cases
    num_cases = int(input())

    # Loop through the test cases
    for _ in range(num_cases):
        # Read the input for the current test case
        r, b, k = map(int, input().split())

        # Solve the current test case
        result = solve(r, b, k)

        # Print the result
        print(result)

if __name__ == '__main__':
    main()

