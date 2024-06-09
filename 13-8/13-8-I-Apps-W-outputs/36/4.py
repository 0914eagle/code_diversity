
def get_min_m(n, k):
    # Initialize the minimum m as 1
    m = 1

    # Iterate until we find a valid solution
    while True:
        # Create a set of integers from 1 to m
        integers = set(range(1, m + 1))

        # Initialize a list to store the sets
        sets = []

        # Iterate through the integers and create sets of rank k
        for i in integers:
            # Find the gcd of the current integer with all the other integers
            gcd = 1
            for j in integers:
                if i != j:
                    gcd = max(gcd, gcd_recursive(i, j))

            # If the gcd is equal to k, add the integer to the current set
            if gcd == k:
                sets.append([i])

        # If we have found n sets of rank k, return the minimum m
        if len(sets) == n:
            return m

        # Increase m by 1 and try again
        m += 1

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

n, k = map(int, input().split())
print(get_min_m(n, k))

