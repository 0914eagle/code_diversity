
def is_execution_unavoidable(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Iterate from 0 to 10^100
    for i in range(10**100):
        # If the current plank is divisible by r, paint it red
        if i % r == 0:
            painted_planks.append("R")
        # If the current plank is divisible by b, paint it blue
        elif i % b == 0:
            painted_planks.append("B")
        # If the current plank is divisible by both r and b, paint it randomly
        elif i % r == 0 and i % b == 0:
            import random
            if random.randint(0, 1) == 0:
                painted_planks.append("R")
            else:
                painted_planks.append("B")
        # If the current plank is not divisible by r or b, do not paint it
        else:
            continue

    # Iterate through the list of painted planks and check if there are k consecutive planks with the same color
    for i in range(len(painted_planks) - k + 1):
        # If the current plank is the same as the next k - 1 planks, return True
        if all(painted_planks[i] == painted_planks[j] for j in range(i + 1, i + k)):
            return True

    # If no consecutive planks with the same color are found, return False
    return False

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the input
        r, b, k = map(int, input().split())

        # Check if the execution is unavoidable
        if is_execution_unavoidable(r, b, k):
            print("REBEL")
        else:
            print("OBEY")

if __name__ == '__main__':
    main()

