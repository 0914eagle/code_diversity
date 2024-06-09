
def f1(n):
    # Initialize an empty stack
    stack = []
    
    # Iterate through the input operations
    for i in range(n):
        # Get the operation and the accompanying stack labels
        operation, stack_labels = input().split()
        
        # Check the type of operation
        if operation == "a":
            # Add the current step to the stack
            stack.append(i)
        elif operation == "b":
            # Remove the top element from the stack and print it
            print(stack.pop())
        elif operation == "c":
            # Get the second stack label and count the number of elements in common with the current stack
            stack_label2 = int(stack_labels[1])
            count = 0
            for element in stack:
                if element in stacks[stack_label2]:
                    count += 1
            # Print the number of elements in common
            print(count)
        else:
            raise ValueError("Invalid operation")
    
    # Return the final stack
    return stack

def f2(stacks):
    # Initialize the number of operations of type 2 and 3
    num_op2 = 0
    num_op3 = 0
    
    # Iterate through the input operations
    for i in range(len(stacks)):
        # Get the operation and the accompanying stack labels
        operation, stack_labels = input().split()
        
        # Check the type of operation
        if operation == "a":
            # Add the current step to the stack
            stacks[i].append(i)
        elif operation == "b":
            # Remove the top element from the stack and print it
            print(stacks[i].pop())
            num_op2 += 1
        elif operation == "c":
            # Get the second stack label and count the number of elements in common with the current stack
            stack_label2 = int(stack_labels[1])
            count = 0
            for element in stacks[i]:
                if element in stacks[stack_label2]:
                    count += 1
            # Print the number of elements in common
            print(count)
            num_op3 += 1
        else:
            raise ValueError("Invalid operation")
    
    # Return the number of operations of type 2 and 3
    return num_op2, num_op3

if __name__ == '__main__':
    n = int(input())
    stacks = [[] for _ in range(n)]
    f1(n)
    num_op2, num_op3 = f2(stacks)
    print(num_op2)
    print(num_op3)

