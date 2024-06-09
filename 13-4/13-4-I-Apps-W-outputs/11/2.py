
def get_largest_xor_sum(n, k):
    # Initialize an empty list to store the candies
    candies = []
    
    # Iterate from 1 to n, where n is the number of candies
    for i in range(1, n + 1):
        # If the number of candies taken so far is less than k, add the current candy to the list
        if len(candies) < k:
            candies.append(i)
        # Otherwise, check if the current candy has a higher tastiness than the current xor-sum
        else:
            xor_sum = 0
            for candy in candies:
                xor_sum ^= candy
            if xor_sum < i:
                candies.pop(0)
                candies.append(i)
    
    # Return the final xor-sum
    xor_sum = 0
    for candy in candies:
        xor_sum ^= candy
    return xor_sum

