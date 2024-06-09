
def get_suitable_values(n, k, c):
    # Sort the coins in descending order
    c.sort(reverse=True)
    # Initialize a set to store the suitable values
    suitable_values = set()
    # Initialize a variable to store the current sum
    current_sum = 0
    # Iterate through the coins
    for i in range(n):
        # If the current sum is less than the price, add the value of the current coin to the current sum
        if current_sum < k:
            current_sum += c[i]
        # If the current sum is equal to the price, add the value of the current coin to the suitable values set
        elif current_sum == k:
            suitable_values.add(c[i])
        # If the current sum is greater than the price, break the loop
        else:
            break
    # Return the suitable values set
    return suitable_values

