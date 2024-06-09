
def max_profit(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    chosen_producer, chosen_consumer = None, None

    # Iterate over each producer company
    for producer in producer_companies:
        # Iterate over each consumer company
        for consumer in consumer_companies:
            # Calculate the profit for this pair of producer and consumer companies
            profit = producer.price - consumer.price

            # Check if the profit is greater than the current maximum profit
            if profit > max_profit:
                # If so, update the maximum profit and the chosen producer and consumer companies
                max_profit = profit
                chosen_producer = producer
                chosen_consumer = consumer

    # Return the maximum profit and the chosen producer and consumer companies
    return max_profit, chosen_producer, chosen_consumer

