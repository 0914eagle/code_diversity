
def f1(N, steps):
    # Initialize an empty stack
    stack = []
    
    # Iterate through the steps
    for step in steps:
        # If the step is of type 1, add the current stack to the stack
        if step[0] == "a":
            stack.append(stack)
        # If the step is of type 2, remove the top element from the stack
        elif step[0] == "b":
            stack.pop()
        # If the step is of type 3, count the number of elements in common with the other stack
        elif step[0] == "c":
            other_stack = stack[int(step[2])]
            count = 0
            for element in stack:
                if element in other_stack:
                    count += 1
            print(count)

def f2(N, steps):
    # Initialize an empty stack
    stack = []
    
    # Iterate through the steps
    for step in steps:
        # If the step is of type 1, add the current stack to the stack
        if step[0] == "a":
            stack.append(stack)
        # If the step is of type 2, remove the top element from the stack and print it
        elif step[0] == "b":
            print(stack.pop())
        # If the step is of type 3, count the number of elements in common with the other stack
        elif step[0] == "c":
            other_stack = stack[int(step[2])]
            count = 0
            for element in stack:
                if element in other_stack:
                    count += 1
            print(count)

if __name__ == '__main__':
    N = int(input())
    steps = []
    for i in range(N):
        steps.append(input().split())
    f1(N, steps)
    f2(N, steps)

