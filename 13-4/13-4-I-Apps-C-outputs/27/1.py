
def get_longest_delivery_time(customers):
    # Initialize the longest delivery time for each company to 0
    longest_delivery_time_company_1 = 0
    longest_delivery_time_company_2 = 0

    # Iterate through each customer
    for i in range(len(customers)):
        # Get the current customer's position
        current_customer = customers[i]

        # Initialize the shortest distance to the next customer of the same company to infinity
        shortest_distance_same_company = float('inf')

        # Initialize the shortest distance to the next customer of the other company to infinity
        shortest_distance_other_company = float('inf')

        # Iterate through the remaining customers
        for j in range(i+1, len(customers)):
            # Get the next customer's position
            next_customer = customers[j]

            # Calculate the distance between the current customer and the next customer
            distance = abs(current_customer[0] - next_customer[0]) + abs(current_customer[1] - next_customer[1])

            # If the next customer is of the same company, update the shortest distance to the next customer of the same company
            if current_customer[0] == next_customer[0] or current_customer[1] == next_customer[1]:
                shortest_distance_same_company = min(shortest_distance_same_company, distance)

            # If the next customer is of the other company, update the shortest distance to the next customer of the other company
            else:
                shortest_distance_other_company = min(shortest_distance_other_company, distance)

        # Update the longest delivery time for each company
        longest_delivery_time_company_1 = max(longest_delivery_time_company_1, shortest_distance_same_company)
        longest_delivery_time_company_2 = max(longest_delivery_time_company_2, shortest_distance_other_company)

    # Return the longest delivery time required by each company
    return (longest_delivery_time_company_1, longest_delivery_time_company_2)

def main():
    # Read the number of customers and their positions from stdin
    num_customers = int(input())
    customers = []
    for i in range(num_customers):
        x, y = map(int, input().split())
        customers.append((x, y))

    # Call the function to get the longest delivery time required by each company
    longest_delivery_time_company_1, longest_delivery_time_company_2 = get_longest_delivery_time(customers)

    # Print the longest delivery time required by each company
    print(longest_delivery_time_company_1)
    print(longest_delivery_time_company_2)

if __name__ == '__main__':
    main()

