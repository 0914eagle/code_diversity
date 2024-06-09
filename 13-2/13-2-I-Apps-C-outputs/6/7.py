
def get_max_customers(customers, clothing):
    # Initialize variables
    max_customers = 0
    current_customers = 0
    current_clothing = []
    time = 0

    # Sort customers by arrival time
    customers.sort(key=lambda x: x[1])

    # Loop through customers
    for customer in customers:
        # If the customer's arrival time is greater than the current time, wait
        if customer[1] > time:
            time = customer[1]

        # If the customer's clothing type is not currently being worn, put it on
        if customer[0] not in current_clothing:
            current_clothing.append(customer[0])
            time += clothing[customer[0] - 1][0]

        # If the customer's clothing type is currently being worn, remove it and put on a different one
        else:
            current_clothing.remove(customer[0])
            time += clothing[customer[0] - 1][1]
            current_clothing.append(customer[0])
            time += clothing[customer[0] - 1][0]

        # Increment the number of customers served
        current_customers += 1

        # Update the maximum number of customers served
        max_customers = max(max_customers, current_customers)

    return max_customers

def main():
    customers = []
    clothing = []

    # Read the number of customers and clothing types
    num_customers, num_clothing = map(int, input().split())

    # Read the required time to put on and remove each type of clothing
    for i in range(num_clothing):
        clothing.append(list(map(int, input().split())))

    # Read the customers
    for i in range(num_customers):
        customers.append(list(map(int, input().split())))

    # Get the maximum number of customers Fluttershy can serve
    max_customers = get_max_customers(customers, clothing)

    # Print the result
    print(max_customers)

if __name__ == '__main__':
    main()

