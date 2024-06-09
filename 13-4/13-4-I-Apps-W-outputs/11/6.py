
def get_largest_xor_sum(n, k):
    # Initialize an empty list to store the candies
    candies = []
    
    # Iterate from 1 to n, which represents the number of candies available
    for i in range(1, n + 1):
        # Check if the current candy is already present in the list
        if i not in candies:
            # Add the current candy to the list
            candies.append(i)
        
        # Check if the length of the list is equal to k, which represents the number of candies that can be taken
        if len(candies) == k:
            # Break the loop
            break
    
    # Initialize a variable to store the xor-sum
    xor_sum = 0
    
    # Iterate through the list of candies
    for i in range(len(candies)):
        # Calculate the xor-sum of the current candy and the previous candy
        xor_sum ^= candies[i]
    
    # Return the xor-sum
    return xor_sum

