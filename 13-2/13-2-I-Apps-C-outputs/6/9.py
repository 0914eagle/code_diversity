
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
        
        # Remove the current type of clothing if it is not the customer's type
        for clothing_type in dressing_time:
            if clothing_type != customer[0]:
                dressing_time[clothing_type] += dressing_time[clothing_type]
        
        # Increment the number of customers served
        num_customers_served += 1
    
    # Return the maximum number of customers served
    return num_customers_served

def main():
    num_customers, num_clothing_types = map(int, input().split())
    dressing_time = {}
    for i in range(num_clothing_types):
        dressing_time[i+1] = int(input())
    
    customers = []
    for i in range(num_customers):
        customer_type, arrival_time = map(int, input().split())
        customers.append((customer_type, arrival_time))
    
    print(get_max_customers(customers, dressing_time))

if __name__ == '__main__':
    main()

