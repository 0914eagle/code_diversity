
def solve(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    chosen_producer = None
    chosen_consumer = None

    # Iterate over each producer company
    for producer in producer_companies:
        # Iterate over each consumer company
        for consumer in consumer_companies:
            # Calculate the profit for this combination of producer and consumer
            profit = producer["price"] - consumer["price"]

            # Check if this is the maximum profit so far
            if profit > max_profit:
                max_profit = profit
                chosen_producer = producer
                chosen_consumer = consumer

    # Return the maximum profit and the chosen producer and consumer companies
    return max_profit, chosen_producer, chosen_consumer

