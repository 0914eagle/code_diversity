
def find_max_raspberry(n, c, x):
    # Initialize variables
    max_profit = 0
    current_profit = 0
    raspberry_left = 0
    day = 1

    # Loop through the prices
    for i in range(n):
        # Check if the bear has enough raspberry to lend a barrel
        if raspberry_left >= c:
            # Calculate the profit from selling the barrel
            current_profit += x[i] - c
            # Subtract the cost of renting the barrel from the raspberry left
            raspberry_left -= c
            # Increment the day
            day += 1

        # Check if the bear has enough raspberry to buy a new barrel
        elif raspberry_left > 0:
            # Calculate the profit from buying a new barrel
            current_profit += x[i] - raspberry_left
            # Set the raspberry left to 0
            raspberry_left = 0
            # Increment the day
            day += 1

        # Check if the bear has run out of raspberry
        else:
            # Break the loop
            break

    # Return the maximum profit
    return current_profit

