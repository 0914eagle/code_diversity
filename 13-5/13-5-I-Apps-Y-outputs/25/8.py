
def get_final_sale_price(events):
    # Initialize variables
    total_shares = 0
    total_cost = 0
    total_profit = 0
    taxes = 0.3

    # Iterate through the events
    for event in events:
        # Buy event
        if event[0] == "buy":
            total_shares += event[1]
            total_cost += event[2] * event[1]
        # Sell event
        elif event[0] == "sell":
            total_profit += (event[2] - (total_cost / total_shares)) * event[1]
        # Split event
        elif event[0] == "split":
            total_shares *= event[1]
            total_cost = total_cost / event[1]
        # Merge event
        elif event[0] == "merge":
            total_shares = (total_shares // event[1]) * event[1] + (total_shares % event[1])
            total_cost = total_cost * event[1]
        # Die event
        elif event[0] == "die":
            total_profit += (event[1] - (total_cost / total_shares)) * total_shares
            break

    # Calculate the final sale price
    final_sale_price = total_profit * (1 - taxes)

    return final_sale_price

