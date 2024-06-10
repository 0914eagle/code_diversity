
def get_maximum_profit(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over all possible producer and consumer combinations
    for producer in producer_companies:
        for consumer in consumer_companies:
            # Calculate the profit for this combination
            profit = calculate_profit(producer, consumer)

            # Check if the profit is greater than the current maximum profit
            if profit > max_profit:
                max_profit = profit
                selected_producer = producer
                selected_consumer = consumer

    # Return the maximum profit and the selected producer and consumer companies
    return max_profit, selected_producer, selected_consumer

def calculate_profit(producer, consumer):
    # Calculate the number of widgets that can be sold
    num_widgets = min(producer["quantity"], consumer["quantity"])

    # Calculate the profit for this combination
    profit = num_widgets * (producer["price"] - consumer["price"])

    return profit

def main():
    # Read the input
    num_producer_companies, num_consumer_companies = map(int, input().split())
    producer_companies = []
    for _ in range(num_producer_companies):
        price, quantity = map(int, input().split())
        producer_companies.append({"price": price, "quantity": quantity})
    consumer_companies = []
    for _ in range(num_consumer_companies):
        price, quantity = map(int, input().split())
        consumer_companies.append({"price": price, "quantity": quantity})

    # Get the maximum profit and the selected producer and consumer companies
    max_profit, selected_producer, selected_consumer = get_maximum_profit(producer_companies, consumer_companies)

    # Print the result
    print(max_profit)

if __name__ == '__main__':
    main()

