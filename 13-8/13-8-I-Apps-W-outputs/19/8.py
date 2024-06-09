
def solve(n, v, sellers):
    # Initialize variables
    p = 0
    q = []

    # Iterate over each seller
    for i in range(n):
        # Find the highest price the seller is offering
        highest_price = max(sellers[i])

        # Check if the highest price is less than or equal to Valera's money
        if highest_price <= v:
            # Increment the number of sellers Valera can make a deal with
            p += 1

            # Add the seller's number to the list of sellers Valera can make a deal with
            q.append(i+1)

    # Sort the list of sellers Valera can make a deal with in increasing order
    q.sort()

    # Return the number of sellers Valera can make a deal with and the list of sellers
    return p, q

