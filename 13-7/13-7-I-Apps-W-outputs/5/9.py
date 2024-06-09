
def get_surviving_islands(num_islands, island_info):
    # Initialize a list to keep track of the number of goods received by each island
    goods_received = [0] * num_islands
    # Initialize a list to keep track of the number of islands that have collapsed
    collapsed_islands = 0

    # Loop through each island
    for i in range(num_islands):
        # Get the threshold and number of incoming goods for the current island
        threshold, num_incoming_goods = island_info[i]
        # Check if the current island has collapsed
        if collapsed_islands > i:
            # If the current island has collapsed, skip it
            continue
        # Check if the current island has received enough goods to survive
        if goods_received[i] >= threshold:
            # If the current island has received enough goods, continue to the next island
            continue
        # If the current island has not received enough goods, mark it as collapsed
        collapsed_islands += 1
        # Loop through the incoming goods for the current island
        for j in range(num_incoming_goods):
            # Get the island number and amount of goods received from the current island
            incoming_island, incoming_goods = island_info[i][j + 2]
            # Check if the incoming island has collapsed
            if collapsed_islands > incoming_island:
                # If the incoming island has collapsed, skip it
                continue
            # Add the amount of goods received from the incoming island to the total goods received by the current island
            goods_received[i] += incoming_goods

    # Return the number of islands that have not collapsed
    return num_islands - collapsed_islands

