
def get_summary_price(n, k, c, id):
    # Initialize the summary price to 0
    summary_price = 0
    
    # Iterate over each pair of cities
    for i in range(n):
        for j in range(i+1, n):
            # If there is a road between the two cities
            if j == i+1 or i == 0:
                # Add the product of their beauty values to the summary price
                summary_price += c[i] * c[j]
    
    # Return the summary price
    return summary_price

