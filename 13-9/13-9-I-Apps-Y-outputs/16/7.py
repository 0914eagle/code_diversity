
def get_stock_price(events):
    # Initialize the stock price and the number of shares
    stock_price = 0
    num_shares = 0
    
    # Iterate through the events
    for event in events:
        # If the event is a buy event, update the stock price and the number of shares
        if event[0] == "buy":
            stock_price = (stock_price * num_shares + event[2] * event[1]) / (num_shares + event[1])
            num_shares += event[1]
        # If the event is a sell event, update the stock price and the number of shares
        elif event[0] == "sell":
            stock_price = (stock_price * num_shares - event[2] * event[1]) / (num_shares - event[1])
            num_shares -= event[1]
        # If the event is a split event, multiply the stock price and the number of shares by the split ratio
        elif event[0] == "split":
            stock_price *= event[1]
            num_shares *= event[1]
        # If the event is a merge event, divide the stock price and the number of shares by the merge ratio
        elif event[0] == "merge":
            stock_price /= event[1]
            num_shares /= event[1]
    
    # Return the final stock price
    return stock_price

def get_taxed_profit(stock_price, num_shares, death_price):
    # Calculate the untaxed profit
    untaxed_profit = num_shares * (death_price - stock_price)
    
    # Apply the capital gains tax
    taxed_profit = untaxed_profit * 0.3
    
    # Return the taxed profit
    return taxed_profit

def get_final_sale_price(events, death_price):
    # Get the stock price and the number of shares before the death event
    stock_price = get_stock_price(events[:-1])
    num_shares = get_num_shares(events[:-1])
    
    # Get the taxed profit
    taxed_profit = get_taxed_profit(stock_price, num_shares, death_price)
    
    # Return the final sale price
    return stock_price + taxed_profit

def get_num_shares(events):
    # Initialize the number of shares
    num_shares = 0
    
    # Iterate through the events
    for event in events:
        # If the event is a buy event, update the number of shares
        if event[0] == "buy":
            num_shares += event[1]
        # If the event is a sell event, update the number of shares
        elif event[0] == "sell":
            num_shares -= event[1]
    
    # Return the number of shares
    return num_shares

if __name__ == '__main__':
    # Read the input
    events = []
    for _ in range(int(input())):
        events.append(input().split())
    
    # Get the final sale price
    final_sale_price = get_final_sale_price(events, int(events[-1][1]))
    
    # Print the output
    print(final_sale_price)

