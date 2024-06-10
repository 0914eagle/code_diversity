
def get_min_steps(a, b):
    # Initialize the minimum number of steps to 0
    min_steps = 0
    # Loop through the array a and compare each element to the corresponding element in array b
    for i in range(len(a)):
        # If the elements are not equal, increase the minimum number of steps by 1
        if a[i] != b[i]:
            min_steps += 1
    # Return the minimum number of steps
    return min_steps

def solve(a, b):
    # Find the minimum number of steps to make a equal to b
    min_steps = get_min_steps(a, b)
    # Return the minimum number of steps
    return min_steps

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))

