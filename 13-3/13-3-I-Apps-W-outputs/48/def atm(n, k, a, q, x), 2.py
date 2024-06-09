
def atm(n, k, a, q, x):
    # Initialize a dictionary to store the number of bills for each denomination
    bills = {a[i]: 0 for i in range(n)}
    # Initialize a list to store the results
    results = []
    
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
                # Check if the number of bills is less than the minimum
                if num_bills < min_bills:
                    # Update the minimum number of bills required
                    min_bills = num_bills
        # Check if the minimum number of bills is less than or equal to k
        if min_bills <= k:
            # Update the dictionary with the number of bills for each denomination
            for j in range(n):
                if a[j] <= x[i]:
                    bills[a[j]] += x[i] // a[j]
            # Add the result to the list
            results.append(min_bills)
        else:
            # Add -1 to the list if the request cannot be fulfilled
            results.append(-1)
    
    return results

