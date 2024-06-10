
def get_final_sale_price(events):
    # Initialize variables
    total_shares = 0
    total_cost = 0
    average_cost = 0
    capital_gains = 0
    taxes = 0

    # Iterate through the events
    for event in events:
        # Get the number of shares and cost per share
        shares, cost = event[1], event[2]

        # Update the total shares and cost
        total_shares += shares
        total_cost += shares * cost

        # Calculate the average cost
        average_cost = total_cost / total_shares

        # If the event is a sell event, calculate the capital gains
        if event[0] == "sell":
            capital_gains += (shares * cost) - (shares * average_cost)

    # Calculate the taxes
    taxes = capital_gains * 0.3

    # Calculate the final sale price
    final_sale_price = total_shares * (average_cost - taxes)

    return final_sale_price

def main():
    # Read the events from input
    events = []
    for _ in range(int(input())):
        events.append(input().split())

    # Calculate the final sale price
    final_sale_price = get_final_sale_price(events)

    # Print the result
    print(f"{final_sale_price:.8f}")

if __name__ == '__main__':
    main()

