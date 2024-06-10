
def get_max_profit(producer_prices, producer_start_days, consumer_prices, consumer_end_days):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over all possible producer and consumer combinations
    for producer_index, producer_price in enumerate(producer_prices):
        for consumer_index, consumer_price in enumerate(consumer_prices):
            # Check if the producer and consumer are compatible (i.e. the producer starts before the consumer ends)
            if producer_start_days[producer_index] <= consumer_end_days[consumer_index]:
                # Calculate the profit for this producer and consumer combination
                profit = producer_price - consumer_price

                # Check if the profit is greater than the current maximum profit
                if profit > max_profit:
                    max_profit = profit
                    selected_producer = producer_index
                    selected_consumer = consumer_index

    # Return the maximum profit and the indices of the selected producer and consumer
    return max_profit, selected_producer, selected_consumer

def main():
    # Read the input data
    num_producers, num_consumers = map(int, input().split())
    producer_prices = []
    producer_start_days = []
    for _ in range(num_producers):
        price, start_day = map(int, input().split())
        producer_prices.append(price)
        producer_start_days.append(start_day)
    consumer_prices = []
    consumer_end_days = []
    for _ in range(num_consumers):
        price, end_day = map(int, input().split())
        consumer_prices.append(price)
        consumer_end_days.append(end_day)

    # Calculate the maximum profit and the indices of the selected producer and consumer
    max_profit, selected_producer, selected_consumer = get_max_profit(producer_prices, producer_start_days, consumer_prices, consumer_end_days)

    # Print the result
    print(max_profit)

if __name__ == '__main__':
    main()

