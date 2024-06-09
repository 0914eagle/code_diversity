
def solve(ring):
    # Initialize a dictionary to store the sums of the pairs
    sums = {}
    
    # Iterate through the input ring
    for i in range(len(ring)):
        # Get the current number and its two neighbors
        num = ring[i]
        left = ring[(i-1)%len(ring)]
        right = ring[(i+1)%len(ring)]
        
        # Calculate the sum of the current number and its neighbors
        sum = num + left + right
        
        # If the sum is not already in the dictionary, add it
        if sum not in sums:
            sums[sum] = [num]
        # If the sum is already in the dictionary, add the current number to the list of numbers with that sum
        else:
            sums[sum].append(num)
    
    # Initialize the output ring
    output = []
    
    # Iterate through the dictionary
    for sum, nums in sums.items():
        # If the list of numbers with the current sum has only one element, it is the original number
        if len(nums) == 1:
            output.append(nums[0])
    
    return output

