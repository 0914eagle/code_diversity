
def atm(n, k, a, q, x):
    # Initialize a dictionary to store the number of bills for each denomination
    bills = {a[i]: 0 for i in range(n)}
    # Initialize a list to store the results
    results = []
    
    # Loop through the requests for cash withdrawal
    for i in range(q):
        # Initialize a variable to store the minimum number of bills required
        min_bills = float('inf')
        # Initialize a variable to store the minimum sum of money that can be withdrawn
        min_sum = float('inf')
        # Loop through the denominations
        for j in range(n):
            # Check if the current denomination is less than or equal to the current request
            if a[j] <= x[i]:
                # Calculate the number of bills required for the current request
                num_bills = x[i] // a[j]
                # Check if the number of bills is less than or equal to k
                if num_bills <= k:
                    # Update the minimum number of bills required
                    min_bills = min(min_bills, num_bills)
                    # Update the minimum sum of money that can be withdrawn
                    min_sum = min(min_sum, x[i])
        # Check if the minimum number of bills required is less than or equal to k
        if min_bills <= k:
            # Add the minimum number of bills required to the dictionary
            bills[a[j]] += min_bills
            # Add the result to the list
            results.append(min_bills)
        # Otherwise, the request cannot be fulfilled
        else:
            # Add -1 to the list
            results.append(-1)
    
    # Return the list of results
    return results

