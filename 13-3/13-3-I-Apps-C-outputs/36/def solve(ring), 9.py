
def solve(ring):
    # Initialize a dictionary to store the sums of the pairs
    sums = {}
    
    # Iterate through the input ring
    for i in range(len(ring)):
        # Get the current number and its two neighbors
        num = ring[i]
        prev = ring[(i - 1) % len(ring)]
        next = ring[(i + 1) % len(ring)]
        
        # Calculate the sum of the current number and its neighbors
        sum = num + prev + next
        
        # If the sum is already in the dictionary, it means we have found a pair
        if sum in sums:
            # Return the original ring
            return [sums[sum], num, prev]
        else:
            # Otherwise, add the sum to the dictionary
            sums[sum] = num
    
    # If no pair is found, return an empty list
    return []

