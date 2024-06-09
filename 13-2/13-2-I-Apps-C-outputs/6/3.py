
def get_max_customers(customers, dressing_time):
    # Sort the customers by their arrival time
    customers.sort(key=lambda x: x[1])
    
    # Initialize the number of customers served to 0
    num_customers_served = 0
    
    # Initialize the current time to 0
    current_time = 0
    
    # Loop through each customer
    for customer in customers:
        # If the customer's arrival time is greater than the current time, wait until the customer arrives
        while customer[1] > current_time:
            current_time += 1
        
        # If the customer's type of clothing is not being worn, put it on
        if customer[0] not in dressing_time:
            dressing_time[customer[0]] = current_time
        
        # Remove the customer's type of clothing if it is already being worn
        if customer[0] in dressing_time:
            current_time = dressing_time[customer[0]] + customer[0]
            del dressing_time[customer[0]]
        
        # Increment the number of customers served
        num_customers_served += 1
    
    # Return the maximum number of customers served
    return num_customers_served

def main():
    # Read the number of customers and the number of types of clothing
    num_customers, num_clothing = map(int, input().split())
    
    # Read the required moments of time to put on and remove each type of clothing
    dressing_time = {}
    for i in range(num_clothing):
        dressing_time[i+1] = int(input())
    
    # Read the descriptions of the customers
    customers = []
    for i in range(num_customers):
        customer = list(map(int, input().split()))
        customers.append(customer)
    
    # Call the function to get the maximum number of customers served
    max_customers = get_max_customers(customers, dressing_time)
    
    # Print the maximum number of customers served
    print(max_customers)

if __name__ == '__main__':
    main()

