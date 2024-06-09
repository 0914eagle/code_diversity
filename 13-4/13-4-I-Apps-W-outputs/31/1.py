
def is_rebel(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Loop through all the planks
    for i in range(10**100):
        # If the index of the plank is divisible by r, paint it red
        if i % r == 0:
            painted_planks.append("R")
        # If the index of the plank is divisible by b, paint it blue
        elif i % b == 0:
            painted_planks.append("B")
        # If the index is divisible by both r and b, choose the color to paint the plank
        elif i % r == 0 and i % b == 0:
            painted_planks.append("R")
        # Otherwise, don't paint the plank
        else:
            continue

    # Loop through the painted planks and check if there are k consecutive planks with the same color
    for i in range(len(painted_planks) - k + 1):
        # If there are k consecutive planks with the same color, return True
        if len(set(painted_planks[i:i+k])) == 1:
            return True

    # If no k consecutive planks with the same color are found, return False
    return False


if __name__ == "__main__":
    # Read the number of test cases
    num_cases = int(input())

    # Loop through the test cases
    for _ in range(num_cases):
        # Read the coefficients r, b, and k
        r, b, k = map(int, input().split())

        # Check if the execution is unavoidable
        if is_rebel(r, b, k):
            print("REBEL")
        # Otherwise, print OBEY
        else:
            print("OBEY")

