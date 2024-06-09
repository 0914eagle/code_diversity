
def get_input():
    N = int(input())
    values = list(map(int, input().split()))
    return N, values

def f1(N, values):
    # Initialize the maximum value as the first value
    max_value = values[0]
    # Loop through the remaining values
    for i in range(1, N):
        # Calculate the average of the current value and the maximum value
        avg = (values[i] + max_value) / 2
        # Update the maximum value if the average is greater than the current maximum value
        if avg > max_value:
            max_value = avg
    return max_value

def f2(N, values):
    # Initialize the maximum value as the first value
    max_value = values[0]
    # Loop through the remaining values
    for i in range(1, N):
        # Calculate the average of the current value and the maximum value
        avg = (values[i] + max_value) / 2
        # Update the maximum value if the average is greater than the current maximum value
        if avg > max_value:
            max_value = avg
    return max_value

if __name__ == '__main__':
    N, values = get_input()
    print(f2(N, values))

