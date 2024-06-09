
def f1(n, a):
    # Initialize a set to store the distinct values of f
    distinct_values = set()

    # Iterate over the sequence
    for i in range(n):
        # Calculate the value of f for the current position
        f_value = gcd(a[i], a[i+1], a[i+2], a[i+3])

        # Add the value of f to the set of distinct values
        distinct_values.add(f_value)

    # Return the number of distinct values of f
    return len(distinct_values)

def f2(n, a):
    # Initialize a dictionary to store the count of each distinct value of f
    distinct_values = {}

    # Iterate over the sequence
    for i in range(n):
        # Calculate the value of f for the current position
        f_value = gcd(a[i], a[i+1], a[i+2], a[i+3])

        # Increment the count of the current value of f
        if f_value in distinct_values:
            distinct_values[f_value] += 1
        else:
            distinct_values[f_value] = 1

    # Return the number of distinct values of f
    return len(distinct_values)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

