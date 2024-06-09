
def solve(A, B, queries):
    # Calculate the height of each Karafs
    heights = [A + (i - 1) * B for i in range(1, 1000001)]
    
    # Iterate over the queries
    for l, t, m in queries:
        # Initialize the maximum number of Karafs that can be eaten
        max_eaten = 0
        
        # Iterate over the possible number of Karafs that can be eaten
        for i in range(l, 1000001):
            # Calculate the number of Karafs that can be eaten with m bites
            num_eaten = min(m, t)
            
            # Check if the current number of Karafs can be eaten
            if heights[i] - num_eaten * B >= 0:
                # Update the maximum number of Karafs that can be eaten
                max_eaten = max(max_eaten, i)
                
                # Break if the maximum number of Karafs has been reached
                if max_eaten == t:
                    break
        
        # Print the answer for the current query
        print(max_eaten)

