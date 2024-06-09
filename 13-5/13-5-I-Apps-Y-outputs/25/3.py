
def get_final_sale_price(events):
    # Initialize variables
    total_shares = 0
    total_cost = 0
    average_cost = 0
    taxes = 0

    # Iterate through the events
    for event in events:
        # Buy event
        if event[0] == "buy":
            total_shares += event[1]
            total_cost += event[2] * event[1]
            average_cost = total_cost / total_shares
        
        # Sell event
        elif event[0] == "sell":
            total_shares -= event[1]
            total_cost -= event[2] * event[1]
            average_cost = total_cost / total_shares
        
        # Split event
        elif event[0] == "split":
            total_shares *= event[1]
            average_cost = total_cost / total_shares
        
        # Merge event
        elif event[0] == "merge":
            total_shares //= event[1]
            average_cost = total_cost / total_shares
        
        # Death event
        elif event[0] == "die":
            taxes = total_cost * 0.3
            total_cost = event[1] * total_shares
    
    # Calculate the final sale price
    final_sale_price = total_cost - taxes
    
    # Return the final sale price
    return final_sale_price

