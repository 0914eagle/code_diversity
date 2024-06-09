
def get_min_price(n, prices, vitamins):
    # Initialize a dictionary to store the number of vitamins obtained by buying each juice
    vitamins_obtained = {}
    for i in range(n):
        vitamins_obtained[i] = 0
        for vitamin in vitamins[i]:
            vitamins_obtained[i] += 1
    
    # Initialize a set to store the indices of juices that contain all three vitamins
    all_vitamins = set()
    for i in range(n):
        if vitamins_obtained[i] == 3:
            all_vitamins.add(i)
    
    # Initialize a dictionary to store the minimum price to obtain all three vitamins by buying each juice
    min_price = {}
    for i in range(n):
        min_price[i] = float('inf')
    
    # Initialize a set to store the indices of juices that have been processed
    processed = set()
    
    # Loop through each juice and calculate the minimum price to obtain all three vitamins by buying it and its cheapest neighbors
    for i in range(n):
        if i not in processed:
            # If the current juice contains all three vitamins, its minimum price is 0
            if i in all_vitamins:
                min_price[i] = 0
            else:
                # Loop through the neighbors of the current juice and calculate the minimum price to obtain all three vitamins by buying it and its cheapest neighbor
                for j in range(i-1, -1, -1):
                    if j in all_vitamins:
                        min_price[i] = min(min_price[i], prices[i] + min_price[j])
                        break
                for j in range(i+1, n):
                    if j in all_vitamins:
                        min_price[i] = min(min_price[i], prices[i] + min_price[j])
                        break
            processed.add(i)
    
    # Return the minimum price to obtain all three vitamins by buying the juice with the lowest price that contains all three vitamins
    return min(min_price[i] for i in all_vitamins) if all_vitamins else -1

