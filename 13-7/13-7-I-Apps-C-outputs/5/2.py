
def get_max_profit(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over each producer company
    for producer in producer_companies:
        # Iterate over each consumer company
        for consumer in consumer_companies:
            # Calculate the profit for this pair of companies
            profit = calculate_profit(producer, consumer)

            # If the profit is greater than the current max profit, update the max profit and the selected companies
            if profit > max_profit:
                max_profit = profit
                selected_producer = producer
                selected_consumer = consumer

    return max_profit

def calculate_profit(producer, consumer):
    # Calculate the profit for this pair of companies
    profit = consumer["price"] - producer["price"]

    # Return the profit
    return profit

def main():
    # Read the input
    m, n = map(int, input().split())
    producer_companies = []
    for i in range(m):
        p, d = map(int, input().split())
        producer_companies.append({"price": p, "day": d})
    consumer_companies = []
    for i in range(n):
        q, e = map(int, input().split())
        consumer_companies.append({"price": q, "day": e})

    # Calculate the max profit
    max_profit = get_max_profit(producer_companies, consumer_companies)

    # Print the result
    print(max_profit)

if __name__ == '__main__':
    main()

