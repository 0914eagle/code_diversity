
def solve(n, d, frogs):
    # Sort the frogs by their leap capacity in descending order
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaped = 0
    
    # Loop through each frog and try to find a combination of frogs that can escape
    for i in range(n):
        # Check if the current frog has a leap capacity greater than the depth of the pit
        if frogs[i][0] > d:
            # If so, add the current frog to the list of escaped frogs
            max_escaped += 1
        else:
            # If not, try to find a combination of frogs that can escape by climbing on top of the current frog
            for j in range(i+1, n):
                # Check if the weight of the current frog and the weight of the frog on top of it does not exceed the maximum weight limit
                if frogs[i][1] + frogs[j][1] <= 1000000:
                    # If so, add the current frog and the frog on top of it to the list of escaped frogs
                    max_escaped += 2
                    break
    
    return max_escaped

