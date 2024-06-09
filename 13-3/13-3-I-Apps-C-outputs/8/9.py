
def solve(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over each producer company
    for producer in producer_companies:
        # Iterate over each consumer company
        for consumer in consumer_companies:
            # Calculate the profit for this pair of producer and consumer companies
            profit = calculate_profit(producer, consumer)

            # Check if the profit is greater than the current maximum profit
            if profit > max_profit:
                # Update the maximum profit and the selected producer and consumer companies
                max_profit = profit
                selected_producer = producer
                selected_consumer = consumer

    # Return the maximum profit and the selected producer and consumer companies
    return max_profit, selected_producer, selected_consumer

def calculate_profit(producer, consumer):
    # Calculate the profit for this pair of producer and consumer companies
    profit = 0

    # Iterate over each day
    for day in range(producer["start_day"], consumer["end_day"] + 1):
        # Check if the producer is delivering widgets on this day
        if day >= producer["start_day"] and day <= producer["end_day"]:
            # Calculate the profit for this day
            profit += producer["price"] - consumer["price"]

    # Return the profit
    return profit

