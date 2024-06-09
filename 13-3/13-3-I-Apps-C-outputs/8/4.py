
def max_profit(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over each producer company
    for producer in producer_companies:
        # Iterate over each consumer company
        for consumer in consumer_companies:
            # Calculate the profit for this combination of producer and consumer
            profit = producer["price"] - consumer["price"]

            # Check if the profit is greater than the current maximum profit
            if profit > max_profit:
                # Update the maximum profit and the selected producer and consumer
                max_profit = profit
                selected_producer = producer
                selected_consumer = consumer

    # Return the maximum profit and the selected producer and consumer
    return max_profit, selected_producer, selected_consumer

