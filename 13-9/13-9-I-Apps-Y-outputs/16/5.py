
def calculate_final_sale_price(event_history):
    # Initialize variables to track the number of shares and their average cost
    num_shares = 0
    total_cost = 0
    
    # Iterate through the event history
    for event in event_history:
        # Check if the event is a buy event
        if event[0] == "buy":
            # Add the number of shares bought to the total number of shares
            num_shares += event[1]
            # Add the cost of the shares to the total cost
            total_cost += event[2] * event[1]
        # Check if the event is a sell event
        elif event[0] == "sell":
            # Subtract the number of shares sold from the total number of shares
            num_shares -= event[1]
            # Subtract the cost of the shares from the total cost
            total_cost -= event[2] * event[1]
        # Check if the event is a split event
        elif event[0] == "split":
            # Multiply the number of shares by the split factor
            num_shares *= event[1]
            # Divide the total cost by the split factor
            total_cost /= event[1]
        # Check if the event is a merge event
        elif event[0] == "merge":
            # Divide the number of shares by the merge factor
            num_shares /= event[1]
            # Multiply the total cost by the merge factor
            total_cost *= event[1]
    
    # Calculate the final sale price as the total cost divided by the number of shares
    final_sale_price = total_cost / num_shares
    
    # Return the final sale price
    return final_sale_price

def calculate_tax_on_profit(final_sale_price, death_price):
    # Calculate the profit as the difference between the final sale price and the death price
    profit = final_sale_price - death_price
    
    # Calculate the tax as 30% of the profit
    tax = profit * 0.3
    
    # Return the tax
    return tax

def main():
    # Read the event history from stdin
    event_history = [tuple(map(int, line.split())) for line in sys.stdin.read().splitlines()]
    
    # Calculate the final sale price
    final_sale_price = calculate_final_sale_price(event_history)
    
    # Calculate the tax on the profit
    tax = calculate_tax_on_profit(final_sale_price, death_price=42)
    
    # Print the total amount obtained after taxes
    print(final_sale_price - tax)

if __name__ == '__main__':
    main()

