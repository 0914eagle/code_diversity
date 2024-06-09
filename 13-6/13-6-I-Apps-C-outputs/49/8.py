
def f1(N):
    # Initialize an empty stack with number 0
    stack = [0]
    
    # Iterate through the given steps
    for i in range(1, N+1):
        # Check the type of operation
        if stack[i-1] == 'a':
            # Operation type 1: Place number i on top of the new stack
            stack.append(i)
        elif stack[i-1] == 'b':
            # Operation type 2: Remove the number from the top of the new stack
            stack.pop()
        elif stack[i-1] == 'c':
            # Operation type 3: Count how many different numbers exist that are in the new stack and in the stack denoted with w
            w = int(stack[i-1][2])
            count = 0
            for j in range(len(stack)):
                if stack[j] in stack[w:]:
                    count += 1
            print(count)
        else:
            # Invalid operation
            print(-1)
    return stack

def f2(stack):
    # Print the required number for each operation type 2 or 3
    for i in range(len(stack)):
        if stack[i] == 'b' or stack[i] == 'c':
            print(stack[i-1])
    return stack

if __name__ == '__main__':
    N = int(input())
    stack = f1(N)
    f2(stack)

