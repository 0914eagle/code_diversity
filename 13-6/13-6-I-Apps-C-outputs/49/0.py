
def f1(N):
    # Initialize an empty stack
    stack = []
    
    # Iterate through the input operations
    for i in range(N):
        # Read the operation type and stack labels
        op, v, w = input().split()
        v, w = int(v), int(w)
        
        # Perform the operation
        if op == "a":
            # Add a new stack with label v
            stack.append(v)
        elif op == "b":
            # Remove the top element from stack v
            stack[v].pop()
        elif op == "c":
            # Count the number of elements in common between stack v and w
            count = 0
            for elem in stack[v]:
                if elem in stack[w]:
                    count += 1
            print(count)
            
def f2(...):
    # Your code here

if __name__ == '__main__':
    N = int(input())
    f1(N)

