
def get_largest_xor_sum(n, k):
    # Convert the input strings to integers
    n = int(n)
    k = int(k)
    
    # Initialize a list to store the tastiness of each candy
    candies = []
    
    # Iterate from 1 to n and add the tastiness of each candy to the list
    for i in range(1, n+1):
        candies.append(i)
    
    # Sort the list of candies in descending order of tastiness
    candies.sort(reverse=True)
    
    # Initialize a variable to store the largest xor-sum
    largest_xor_sum = 0
    
    # Iterate through the list of candies and calculate the xor-sum of the first k candies
    for i in range(k):
        largest_xor_sum ^= candies[i]
    
    # Return the largest xor-sum
    return largest_xor_sum

