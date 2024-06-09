
def f1(n, a):
    # Initialize a set to store the distinct values of f
    distinct_values = set()

    # Iterate over the sequence
    for i in range(n):
        for j in range(i+1, n+1):
            # Calculate the value of f(i, j)
            f_value = gcd(a[i], a[i+1], a[j-1], a[j])

            # Add the value to the set of distinct values
            distinct_values.add(f_value)

    # Return the number of distinct values
    return len(distinct_values)

def f2(n, a):
    # Initialize a dictionary to store the counts of each distinct value of f
    distinct_values = {}

    # Iterate over the sequence
    for i in range(n):
        for j in range(i+1, n+1):
            # Calculate the value of f(i, j)
            f_value = gcd(a[i], a[i+1], a[j-1], a[j])

            # Increment the count of the value in the dictionary
            if f_value in distinct_values:
                distinct_values[f_value] += 1
            else:
                distinct_values[f_value] = 1

    # Return the number of distinct values
    return len(distinct_values)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

