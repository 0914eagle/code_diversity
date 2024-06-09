
def calculate_profit(events):
    # Initialize variables
    shares_bought = 0
    shares_sold = 0
    average_cost = 0
    total_profit = 0
    taxes = 0

    # Iterate through the events
    for event in events:
        # Check if the event is a buy
        if event[0] == "buy":
            # Increment the number of shares bought
            shares_bought += event[1]
            # Calculate the average cost of the shares
            average_cost = (average_cost * shares_sold + event[2] * event[1]) / (shares_sold + event[1])
        # Check if the event is a sell
        elif event[0] == "sell":
            # Increment the number of shares sold
            shares_sold += event[1]
            # Calculate the profit from the sale
            profit = event[2] * event[1] - average_cost * event[1]
            # Add the profit to the total profit
            total_profit += profit
        # Check if the event is a split
        elif event[0] == "split":
            # Increment the number of shares
            shares_bought *= event[1]
            shares_sold *= event[1]
        # Check if the event is a merge
        elif event[0] == "merge":
            # Decrement the number of shares
            shares_bought //= event[1]
            shares_sold //= event[1]
        # Check if the event is a die
        elif event[0] == "die":
            # Calculate the final profit
            final_profit = event[1] * shares_sold - taxes
            # Return the final profit
            return final_profit
        # Calculate the taxes
        taxes = total_profit * 0.3

    # Return the total profit
    return total_profit

def main():
    # Read the input
    events = []
    for _ in range(int(input())):
        events.append(input().split())
    # Calculate the profit
    profit = calculate_profit(events)
    # Print the result
    print(f"{profit:.8f}")

if __name__ == '__main__':
    main()

