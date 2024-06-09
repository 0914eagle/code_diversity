
def f1(N, K):
    # Initialize the minimum value as the starting value
    min_value = 1
    # Loop through the number of operations
    for i in range(N):
        # If the current value is even, double it
        if min_value % 2 == 0:
            min_value *= 2
        # If the current value is odd, add K to it
        else:
            min_value += K
    # Return the minimum value
    return min_value

def f2(N, K):
    # Initialize the minimum value as the starting value
    min_value = 1
    # Loop through the number of operations
    for i in range(N):
        # If the current value is odd, add K to it
        if min_value % 2 == 1:
            min_value += K
        # If the current value is even, double it
        else:
            min_value *= 2
    # Return the minimum value
    return min_value

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(f1(N, K))
    print(f2(N, K))

