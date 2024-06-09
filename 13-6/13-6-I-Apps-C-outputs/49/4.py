
def f1(N):
    # Initialize an empty stack
    stack = []
    # Iterate through the steps of the game
    for i in range(N):
        # Get the current step
        step = input()
        # Check the type of operation
        if step[0] == 'a':
            # Add the current step to the stack
            stack.append(i)
        elif step[0] == 'b':
            # Remove the top element from the stack
            stack.pop()
        elif step[0] == 'c':
            # Get the two stacks involved in the operation
            stack1 = step[2]
            stack2 = step[3]
            # Count the number of elements in both stacks
            count = len(set(stack1).intersection(set(stack2)))
            # Print the result
            print(count)

def f2(...):
    ...

if __name__ == '__main__':
    N = int(input())
    f1(N)

