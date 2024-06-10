
def is_rebel(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []

    # Loop through all the planks
    for i in range(10**100):
        # Check if the current plank is divisible by r and b
        if i % r == 0 and i % b == 0:
            # If both conditions are true, choose a color at random
            color = "red" if random.random() > 0.5 else "blue"
        elif i % r == 0:
            # If the current plank is divisible by r, paint it red
            color = "red"
        elif i % b == 0:
            # If the current plank is divisible by b, paint it blue
            color = "blue"
        else:
            # If the current plank is not divisible by either r or b, skip it
            continue

        # Add the painted plank to the list
        painted_planks.append(color)

        # Check if there are k consecutive planks with the same color
        if len(painted_planks) >= k:
            # If there are, return True (the execution is unavoidable)
            return True

    # If we reach this point, return False (the execution is not unavoidable)
    return False

def main():
    # Read the number of test cases
    num_cases = int(input())

    # Loop through each test case
    for _ in range(num_cases):
        # Read the coefficients r, b, and k
        r, b, k = map(int, input().split())

        # Check if the execution is unavoidable
        if is_rebel(r, b, k):
            # If it is, print REBEL
            print("REBEL")
        else:
            # If it's not, print OBEY
            print("OBEY")

if __name__ == "__main__":
    main()

