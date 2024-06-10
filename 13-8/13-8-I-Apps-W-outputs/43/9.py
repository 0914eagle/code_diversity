
def is_rebellious(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Iterate from 0 to 10^100
    for i in range(10**100):
        # If the index is divisible by r, paint the plank red
        if i % r == 0:
            painted_planks.append("R")
        # If the index is divisible by b, paint the plank blue
        elif i % b == 0:
            painted_planks.append("B")
        # If the index is divisible by both r and b, paint the plank according to your preference
        elif i % r == 0 and i % b == 0:
            painted_planks.append("R")
        # Otherwise, don't paint the plank
        else:
            continue

    # Iterate through the painted planks and check if there are k consecutive planks with the same color
    for i in range(len(painted_planks) - k + 1):
        # If there are k consecutive planks with the same color, return True
        if len(set(painted_planks[i:i+k])) == 1:
            return True

    # If there are no k consecutive planks with the same color, return False
    return False

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the input
        r, b, k = map(int, input().split())

        # Check if the execution is unavoidable
        if is_rebellious(r, b, k):
            print("REBEL")
        else:
            print("OBEY")

if __name__ == '__main__':
    main()

