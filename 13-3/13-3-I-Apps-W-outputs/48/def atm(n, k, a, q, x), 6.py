
def atm(n, k, a, q, x):
    # Initialize a dictionary to store the minimum number of bills for each sum
    min_bills = {}
    for i in range(q):
        # Initialize the minimum number of bills to -1, indicating that it is not possible to get the sum
        min_bills[x[i]] = -1
        # Iterate through the denominations and check if they can be used to get the sum
        for j in range(n):
            if x[i] % a[j] == 0 and x[i] // a[j] <= k:
                # If the denominations can be used to get the sum, update the minimum number of bills
                min_bills[x[i]] = x[i] // a[j]
                break
    return [min_bills[x] for x in x]

