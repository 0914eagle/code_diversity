
def f1(N):
    # Initialize an empty stack
    stack = []
    
    # Iterate through the given steps
    for i in range(N):
        # Get the current step
        step = input()
        
        # Check the type of operation
        if step[0] == "a":
            # Operation of type 1: Place number i on top of the new stack
            stack.append(i)
        elif step[0] == "b":
            # Operation of type 2: Remove the number from the top of the new stack
            stack.pop()
        elif step[0] == "c":
            # Operation of type 3: Count how many different numbers exist that are in the new stack and in the stack denoted with w
            w = int(step[2])
            count = 0
            for num in stack:
                if num in stack[w]:
                    count += 1
            print(count)
        else:
            raise ValueError("Invalid operation type")
    
    return stack

def f2(stack):
    # Output the required number for each operation of type 2 or 3
    for step in stack:
        if step[0] == "b":
            print(step[1])
        elif step[0] == "c":
            print(step[2])
        else:
            raise ValueError("Invalid operation type")
    
    return stack

if __name__ == '__main__':
    N = int(input())
    stack = f1(N)
    f2(stack)

