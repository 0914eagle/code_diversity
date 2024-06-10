
def get_maximum_profit(producer_companies, consumer_companies):
    # Initialize variables
    max_profit = 0
    selected_producer = None
    selected_consumer = None

    # Iterate over all possible producer and consumer combinations
    for producer in producer_companies:
        for consumer in consumer_companies:
            # Calculate the profit for this combination
            profit = producer.price - consumer.price

            # Check if the profit is greater than the current maximum profit
            if profit > max_profit:
                max_profit = profit
                selected_producer = producer
                selected_consumer = consumer

    # Return the maximum profit and the selected producer and consumer companies
    return max_profit, selected_producer, selected_consumer

def main():
    # Read the input
    m, n = map(int, input().split())
    producer_companies = []
    for _ in range(m):
        price, day = map(int, input().split())
        producer_companies.append(ProducerCompany(price, day))
    consumer_companies = []
    for _ in range(n):
        price, day = map(int, input().split())
        consumer_companies.append(ConsumerCompany(price, day))

    # Calculate the maximum profit and the selected producer and consumer companies
    max_profit, selected_producer, selected_consumer = get_maximum_profit(producer_companies, consumer_companies)

    # Print the result
    print(max_profit)

# Define the ProducerCompany and ConsumerCompany classes
class ProducerCompany:
    def __init__(self, price, day):
        self.price = price
        self.day = day

class ConsumerCompany:
    def __init__(self, price, day):
        self.price = price
        self.day = day

if __name__ == '__main__':
    main()

