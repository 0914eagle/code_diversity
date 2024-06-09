
def get_largest_xor_sum(n, k):
    # Initialize an empty list to store the candies
    candies = []
    
    # Iterate from 1 to n, which represents the number of candies
    for i in range(1, n + 1):
        # If the number of candies taken is less than or equal to k, append the current candy to the list
        if len(candies) <= k:
            candies.append(i)
        # If the number of candies taken is greater than k, remove the first candy from the list and append the current candy
        else:
            candies.pop(0)
            candies.append(i)
    
    # Initialize a variable to store the xor-sum
    xor_sum = 0
    
    # Iterate through the list of candies
    for candy in candies:
        # Calculate the xor-sum by taking the bitwise XOR of each candy
        xor_sum ^= candy
    
    # Return the largest xor-sum
    return xor_sum

