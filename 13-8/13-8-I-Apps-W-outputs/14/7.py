
def get_min_steps(a, b):
    # Initialize the minimum number of steps as 0
    min_steps = 0
    # Loop through the elements of the array
    for i in range(len(a)):
        # If the element is not equal to the corresponding element in the target array, add 1 to the minimum number of steps
        if a[i] != b[i]:
            min_steps += 1
    # Return the minimum number of steps
    return min_steps

def solve(n, b):
    # Initialize the array with n zeros
    a = [0] * n
    # Call the get_min_steps function to get the minimum number of steps
    min_steps = get_min_steps(a, b)
    # Return the minimum number of steps
    return min_steps

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    print(solve(n, b))

