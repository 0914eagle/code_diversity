
def calculate_profit(events):
    # Initialize variables
    total_shares = 0
    total_cost = 0
    average_cost = 0
    taxes = 0
    profit = 0

    # Iterate through the events
    for event in events:
        # Get the event type and number of shares
        event_type, shares = event.split()
        shares = int(shares)

        # Buy event
        if event_type == "buy":
            total_shares += shares
            total_cost += shares * average_cost

        # Sell event
        elif event_type == "sell":
            total_shares -= shares
            total_cost -= shares * average_cost

        # Split event
        elif event_type == "split":
            total_shares *= int(shares)
            average_cost /= int(shares)

        # Merge event
        elif event_type == "merge":
            total_shares = int(shares) * (total_shares // int(shares))
            average_cost = total_cost / total_shares

        # Death event
        elif event_type == "die":
            profit = int(shares) - total_cost * 0.3
            break

    # Calculate taxes
    taxes = profit * 0.3

    # Return the profit after taxes
    return profit - taxes

def main():
    # Read the events from stdin
    events = []
    for line in sys.stdin:
        events.append(line.strip())

    # Calculate the profit
    profit = calculate_profit(events)

    # Print the result
    print(f"{profit:.8f}")

if __name__ == "__main__":
    main()

