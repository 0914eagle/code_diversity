
def is_rebel(r, b, k):
    # Initialize variables
    red_planks = []
    blue_planks = []
    painted_planks = []

    # Iterate through all planks
    for i in range(10**100):
        # Check if the current plank is red
        if i % r == 0:
            red_planks.append(i)
        # Check if the current plank is blue
        if i % b == 0:
            blue_planks.append(i)
        # Check if the current plank is painted
        if i % r == 0 or i % b == 0:
            painted_planks.append(i)

    # Sort the painted planks in ascending order
    painted_planks.sort()

    # Initialize variables
    consecutive_red_planks = 0
    consecutive_blue_planks = 0

    # Iterate through the painted planks
    for i in range(len(painted_planks)):
        # Check if the current plank is red
        if painted_planks[i] in red_planks:
            # Increment the number of consecutive red planks
            consecutive_red_planks += 1
            # Check if the number of consecutive red planks is greater than or equal to k
            if consecutive_red_planks >= k:
                return True
        # Check if the current plank is blue
        elif painted_planks[i] in blue_planks:
            # Increment the number of consecutive blue planks
            consecutive_blue_planks += 1
            # Check if the number of consecutive blue planks is greater than or equal to k
            if consecutive_blue_planks >= k:
                return True
        # Check if the current plank is not red or blue
        else:
            # Reset the number of consecutive red and blue planks
            consecutive_red_planks = 0
            consecutive_blue_planks = 0

    # Return False if the execution is unavoidable
    return False

def main():
    # Read the number of test cases
    t = int(input())

    # Iterate through the test cases
    for i in range(t):
        # Read the input
        r, b, k = map(int, input().split())

        # Check if the execution is unavoidable
        if is_rebel(r, b, k):
            # Print REBEL
            print("REBEL")
        else:
            # Print OBEY
            print("OBEY")

if __name__ == '__main__':
    main()

