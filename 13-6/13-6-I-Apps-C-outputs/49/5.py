
def f1(n):
    # Initialize an empty stack
    stack = []
    
    # Iterate through the given steps
    for i in range(n):
        # Get the current step
        step = input()
        
        # If the step is of type 1, add the current index to the stack
        if step[0] == 'a':
            stack.append(i)
        
        # If the step is of type 2, remove the top element from the stack and print it
        elif step[0] == 'b':
            print(stack.pop())
        
        # If the step is of type 3, count the number of elements in common between the current stack and the stack with the given label
        elif step[0] == 'c':
            label = int(step[2])
            count = 0
            for elem in stack:
                if elem in stacks[label]:
                    count += 1
            print(count)
    
    # Return the final stack
    return stack

def f2(n):
    # Initialize a dictionary to store the stacks
    stacks = {i: [] for i in range(n)}
    
    # Iterate through the given steps
    for i in range(n):
        # Get the current step
        step = input()
        
        # If the step is of type 1, add the current index to the stack
        if step[0] == 'a':
            stacks[i].append(i)
        
        # If the step is of type 2, remove the top element from the stack and print it
        elif step[0] == 'b':
            print(stacks[i].pop())
        
        # If the step is of type 3, count the number of elements in common between the current stack and the stack with the given label
        elif step[0] == 'c':
            label = int(step[2])
            count = 0
            for elem in stacks[i]:
                if elem in stacks[label]:
                    count += 1
            print(count)
    
    # Return the final stacks
    return stacks

if __name__ == '__main__':
    n = int(input())
    stack = f1(n)
    stacks = f2(n)

