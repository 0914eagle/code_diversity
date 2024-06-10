
def get_max_profit(producer_prices, producer_start_dates, consumer_prices, consumer_end_dates):
    # Initialize variables
    max_profit = 0
    selected_producer = 0
    selected_consumer = 0

    # Loop through each producer and consumer combination
    for producer in range(len(producer_prices)):
        for consumer in range(len(consumer_prices)):
            # Check if the producer can start delivering widgets on the day the consumer needs them
            if producer_start_dates[producer] <= consumer_end_dates[consumer]:
                # Calculate the profit from this combination
                profit = consumer_prices[consumer] - producer_prices[producer]

                # Check if the profit is higher than the current maximum profit
                if profit > max_profit:
                    max_profit = profit
                    selected_producer = producer
                    selected_consumer = consumer

    # Return the maximum profit and the selected producer and consumer
    return max_profit, selected_producer, selected_consumer

def main():
    # Read the input
    m, n = map(int, input().split())
    producer_prices = []
    producer_start_dates = []
    for _ in range(m):
        producer_prices.append(int(input()))
        producer_start_dates.append(int(input()))
    consumer_prices = []
    consumer_end_dates = []
    for _ in range(n):
        consumer_prices.append(int(input()))
        consumer_end_dates.append(int(input()))

    # Call the get_max_profit function
    max_profit, selected_producer, selected_consumer = get_max_profit(producer_prices, producer_start_dates, consumer_prices, consumer_end_dates)

    # Print the result
    print(max_profit)

if __name__ == '__main__':
    main()

