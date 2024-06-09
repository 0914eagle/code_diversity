
def get_min_price(n, prices, vitamins):
    # Initialize a dictionary to store the count of vitamins
    vitamin_count = {"A": 0, "B": 0, "C": 0}
    
    # Iterate over the vitamins in each juice
    for i in range(n):
        for vitamin in vitamins[i]:
            # If the vitamin is not already in the dictionary, add it
            if vitamin not in vitamin_count:
                vitamin_count[vitamin] = 1
            # If the vitamin is already in the dictionary, increment its count
            else:
                vitamin_count[vitamin] += 1
    
    # Check if all three vitamins are present
    if "A" in vitamin_count and "B" in vitamin_count and "C" in vitamin_count:
        # Return the minimum price
        return min(prices)
    # If not all three vitamins are present, return -1
    else:
        return -1

