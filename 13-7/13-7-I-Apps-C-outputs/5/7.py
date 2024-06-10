
def get_max_profit(producer_prices, consumer_prices, producer_days, consumer_days):
    # Initialize variables
    max_profit = 0
    producer_index = 0
    consumer_index = 0

    # Loop through all possible combinations of producer and consumer companies
    for i in range(len(producer_prices)):
        for j in range(len(consumer_prices)):
            # Calculate the profit for this combination of producer and consumer companies
            profit = (consumer_prices[j] - producer_prices[i]) * (consumer_days[j] - producer_days[i])

            # If the profit is greater than the current maximum profit, update the variables
            if profit > max_profit:
                max_profit = profit
                producer_index = i
                consumer_index = j

    # Return the maximum profit and the indices of the producer and consumer companies with the maximum profit
    return max_profit, producer_index, consumer_index

def main():
    # Read the input data
    m, n = map(int, input().split())
    producer_prices = []
    producer_days = []
    for i in range(m):
        p, d = map(int, input().split())
        producer_prices.append(p)
        producer_days.append(d)
    consumer_prices = []
    consumer_days = []
    for i in range(n):
        q, e = map(int, input().split())
        consumer_prices.append(q)
        consumer_days.append(e)

    # Call the function to get the maximum profit and the indices of the producer and consumer companies with the maximum profit
    max_profit, producer_index, consumer_index = get_max_profit(producer_prices, consumer_prices, producer_days, consumer_days)

    # Print the maximum profit
    print(max_profit)

if __name__ == '__main__':
    main()

