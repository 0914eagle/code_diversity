
def f1(N):
    # Initialize an empty stack with number 0
    stack = [0]
    # Iterate through the given steps
    for i in range(1, N+1):
        # Get the current step
        step = input()
        # Check the type of operation
        if step[0] == "a":
            # Operation of type 1: place number i on top of the new stack
            stack.append(i)
        elif step[0] == "b":
            # Operation of type 2: remove the number from the top of the new stack
            stack.pop()
        elif step[0] == "c":
            # Operation of type 3: count how many different numbers exist that are in the new stack and in the stack denoted with w
            w = int(step[2])
            count = 0
            for num in stack:
                if num in stack[w:] and num not in stack[:w]:
                    count += 1
            print(count)

def f2(...):
    ...

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        f1(N)

