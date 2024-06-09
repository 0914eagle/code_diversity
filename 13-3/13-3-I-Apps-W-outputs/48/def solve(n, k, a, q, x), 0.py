
def solve(n, k, a, q, x):
    # Initialize a dictionary to store the number of bills for each denomination
    bills = {a[i]: 0 for i in range(n)}
    # Loop through the requests for cash withdrawal
    for i in range(q):
        # Initialize a variable to store the minimum number of bills required
        min_bills = float('inf')
        # Loop through the denominations
        for j in range(n):
            # Check if the current denomination is sufficient to cover the request
            if a[j] <= x[i]:
                # Calculate the number of bills required for the current denomination
                num_bills = x[i] // a[j]
                # Check if the number of bills is less than the minimum required
                if num_bills < min_bills:
                    # Update the minimum number of bills required
                    min_bills = num_bills
        # Check if the minimum number of bills is less than or equal to k
        if min_bills <= k:
            # Update the number of bills for each denomination
            for j in range(n):
                bills[a[j]] += min_bills
            # Print the minimum number of bills required
            print(min_bills)
        else:
            # Print -1 if the minimum number of bills is greater than k
            print(-1)
    return bills

