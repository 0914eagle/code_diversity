
def get_min_f(n, a):
    # Initialize the minimum value of f(i, j) to a large number
    min_f = 1000000
    # Loop through all possible values of i and j
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the value of f(i, j)
            f = (i - j) ** 2 + g(i, j, a) ** 2
            # Update the minimum value of f(i, j) if necessary
            if f < min_f and i != j:
                min_f = f
    # Return the minimum value of f(i, j)
    return min_f

def g(i, j, a):
    # Initialize the sum to 0
    sum = 0
    # Loop through all values of k between i and j (inclusive)
    for k in range(min(i, j) + 1, max(i, j) + 1):
        # Add the value of a[k] to the sum
        sum += a[k]
    # Return the sum
    return sum

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_f(n, a))

