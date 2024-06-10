
def get_max_profit(producer_prices, producer_start_dates, consumer_prices, consumer_end_dates):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Loop through each producer and consumer combination
    for producer_index, producer_price in enumerate(producer_prices):
        for consumer_index, consumer_price in enumerate(consumer_prices):
            # Check if the producer starts before the consumer ends
            if producer_start_dates[producer_index] <= consumer_end_dates[consumer_index]:
                # Calculate the profit for this producer and consumer combination
                profit = producer_price - consumer_price

                # Check if the profit is greater than the current max profit
                if profit > max_profit:
                    max_profit = profit
                    selected_producer = producer_index
                    selected_consumer = consumer_index

    # Return the max profit and the selected producer and consumer indices
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

