
def solve(n, v, sellers):
    # Initialize variables
    p = 0
    q = []

    # Iterate over each seller
    for i in range(n):
        # Initialize variables for each seller
        k = sellers[i][0]
        prices = sellers[i][1:]

        # Check if the seller has any items for sale
        if k == 0:
            continue

        # Initialize variables for each item
        min_price = float('inf')
        min_index = 0

        # Find the minimum price of the items
        for j in range(k):
            if prices[j] < min_price:
                min_price = prices[j]
                min_index = j

        # Check if the minimum price is within Valera's budget
        if min_price <= v:
            p += 1
            q.append(i + 1)

    return p, q

