
def get_max_profit(producer_prices, consumer_prices, start_dates, end_dates):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Loop through each producer and consumer combination
    for producer_index, producer_price in enumerate(producer_prices):
        for consumer_index, consumer_price in enumerate(consumer_prices):
            # Check if the producer and consumer are compatible (i.e. the producer starts before the consumer ends and the consumer starts before the producer ends)
            if start_dates[producer_index] <= end_dates[consumer_index] and start_dates[consumer_index] <= start_dates[producer_index]:
                # Calculate the profit for this combination
                profit = producer_price - consumer_price

                # Check if the profit is greater than the current max profit
                if profit > max_profit:
                    max_profit = profit
                    selected_producer = producer_index
                    selected_consumer = consumer_index

    return max_profit, selected_producer, selected_consumer

def main():
    # Read the input
    num_producers, num_consumers = map(int, input().split())
    producer_prices = []
    start_dates = []
    for _ in range(num_producers):
        producer_price, start_date = map(int, input().split())
        producer_prices.append(producer_price)
        start_dates.append(start_date)
    consumer_prices = []
    end_dates = []
    for _ in range(num_consumers):
        consumer_price, end_date = map(int, input().split())
        consumer_prices.append(consumer_price)
        end_dates.append(end_date)

    # Call the function to get the max profit
    max_profit, selected_producer, selected_consumer = get_max_profit(producer_prices, consumer_prices, start_dates, end_dates)

    # Print the result
    print(max_profit)

if __name__ == '__main__':
    main()

