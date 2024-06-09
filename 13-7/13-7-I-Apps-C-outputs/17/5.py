
def solve(orders):
    # Sort the orders by the time they were placed
    orders.sort(key=lambda x: x[0])
    
    # Initialize the delivery schedule with the first order
    schedule = [orders[0]]
    
    # Iterate through the remaining orders
    for order in orders[1:]:
        # Check if the current order can be delivered after the previous order
        if order[1] == schedule[-1][1] and order[0] > schedule[-1][0]:
            # If it can, add it to the delivery schedule
            schedule.append(order)
        else:
            # If it can't, find the closest intersection that can be reached from the previous order
            for i in range(len(schedule)):
                if order[1] == schedule[i][1] and order[0] > schedule[i][0]:
                    # Add the order to the delivery schedule at this intersection
                    schedule.insert(i+1, order)
                    break
    
    # Return the longest wait time
    return max(order[0] - schedule[i][0] for i, order in enumerate(orders))

