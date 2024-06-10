
import math

def solve(events):
    # Initialize variables
    shares = 0
    cost = 0
    taxes = 0
    profit = 0

    # Loop through the events
    for event in events:
        # Check the type of event
        if event[0] == "buy":
            # Buy event, update the number of shares and cost
            shares += event[1]
            cost += event[2] * event[1]
        elif event[0] == "sell":
            # Sell event, update the number of shares and cost
            shares -= event[1]
            cost -= event[2] * event[1]
        elif event[0] == "split":
            # Split event, update the number of shares and cost
            shares *= event[1]
            cost = cost / event[1]
        elif event[0] == "merge":
            # Merge event, update the number of shares and cost
            shares = int(shares / event[1])
            cost = cost * event[1]
        elif event[0] == "die":
            # Die event, calculate the profit and taxes
            profit = event[1] * shares - cost
            taxes = profit * 0.3
            break

    # Calculate the total amount obtained after taxes
    total = profit - taxes

    # Return the total amount
    return total

def main():
    # Read the input
    events = []
    for _ in range(int(input())):
        events.append(input().split())

    # Solve the problem
    total = solve(events)

    # Print the output
    print(f"{total:.8f}")

if __name__ == '__main__':
    main()

