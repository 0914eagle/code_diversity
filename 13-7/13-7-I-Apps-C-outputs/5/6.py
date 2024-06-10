
def get_profit(producer_prices, consumer_prices, producer_start_days, consumer_end_days):
    # Initialize variables
    total_profit = 0
    current_day = 1

    # Loop through each producer and consumer combination
    for producer_index in range(len(producer_prices)):
        for consumer_index in range(len(consumer_prices)):
            # Check if the producer can start delivering widgets on the current day
            if current_day >= producer_start_days[producer_index]:
                # Check if the consumer is willing to buy widgets on the current day
                if current_day <= consumer_end_days[consumer_index]:
                    # Calculate the profit for this producer and consumer combination
                    profit = producer_prices[producer_index] - consumer_prices[consumer_index]

                    # Check if the profit is positive
                    if profit > 0:
                        # Add the profit to the total profit
                        total_profit += profit

    # Return the total profit
    return total_profit

def main():
    # Read the number of producer and consumer companies
    m, n = map(int, input().split())

    # Read the producer prices and start days
    producer_prices = []
    producer_start_days = []
    for i in range(m):
        price, start_day = map(int, input().split())
        producer_prices.append(price)
        producer_start_days.append(start_day)

    # Read the consumer prices and end days
    consumer_prices = []
    consumer_end_days = []
    for i in range(n):
        price, end_day = map(int, input().split())
        consumer_prices.append(price)
        consumer_end_days.append(end_day)

    # Calculate the total profit
    total_profit = get_profit(producer_prices, consumer_prices, producer_start_days, consumer_end_days)

    # Print the total profit
    print(total_profit)

if __name__ == '__main__':
    main()

