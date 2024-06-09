
def f1(N):
    # Initialize an empty stack with label 0
    stacks = [{}]

    # Iterate through the steps of the game
    for i in range(1, N + 1):
        # Get the current step
        step = input()

        # Check the type of operation
        if step[0] == "a":
            # Create a new stack with label i
            stacks.append({})
        elif step[0] == "b":
            # Remove the top element from the stack with label step[1]
            stack = stacks[int(step[1])]
            top = stack.pop()
            print(top)
        elif step[0] == "c":
            # Count the number of elements in common between the stacks with labels step[1] and step[2]
            stack1 = stacks[int(step[1])]
            stack2 = stacks[int(step[2])]
            count = len(set(stack1).intersection(stack2))
            print(count)

if __name__ == "__main__":
    N = int(input())
    f1(N)

