
def max_profit(producer_prices, producer_start_dates, consumer_prices, consumer_end_dates):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over each producer and consumer combination
    for producer_index, producer_price in enumerate(producer_prices):
        for consumer_index, consumer_price in enumerate(consumer_prices):
            # Check if the producer is available on the day the consumer needs the widget
            if producer_start_dates[producer_index] <= consumer_end_dates[consumer_index]:
                # Calculate the profit for this combination
                profit = producer_price - consumer_price

                # Check if the profit is greater than the current maximum profit
                if profit > max_profit:
                    max_profit = profit
                    selected_producer = producer_index
                    selected_consumer = consumer_index

    # Return the maximum profit and the indices of the selected producer and consumer
    return max_profit, selected_producer, selected_consumer

