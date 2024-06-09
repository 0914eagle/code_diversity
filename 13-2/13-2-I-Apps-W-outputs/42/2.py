
def solve(A, B, queries):
    # Calculate the height of each Karafs
    heights = [A + (i - 1) * B for i in range(1, 1000001)]
    
    # Iterate over the queries
    for l, t, m in queries:
        # Initialize the maximum number of Karafs that can be eaten
        max_eaten = 0
        
        # Iterate over the possible number of Karafs that can be eaten
        for i in range(l, 1000001):
            # Check if the current number of Karafs can be eaten
            if heights[i] >= m * B:
                # Update the maximum number of Karafs that can be eaten
                max_eaten = i
            else:
                # Break the loop if the current number of Karafs cannot be eaten
                break
        
        # Check if the maximum number of Karafs that can be eaten is less than or equal to t
        if max_eaten <= t:
            # Print the maximum number of Karafs that can be eaten
            print(max_eaten)
        else:
            # Print -1 if the maximum number of Karafs that can be eaten is greater than t
            print(-1)
            
solve(2, 1, [(1, 5, 3), (3, 3, 10), (7, 10, 2), (6, 4, 8)])
solve(1, 5, [(1, 5, 10), (2, 7, 4)])

