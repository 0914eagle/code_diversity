
def get_max_customers(customers, dressing_times, removing_times):
    # Initialize the number of customers served to 0
    num_customers_served = 0
    
    # Sort the customers by their arrival time
    customers.sort(key=lambda x: x[1])
    
    # Initialize the current time to 0
    current_time = 0
    
    # Loop through each customer
    for customer in customers:
        # Get the type of clothing and arrival time of the customer
        clothing_type, arrival_time = customer[0], customer[1]
        
        # If the customer arrives before the current time, skip them
        if arrival_time < current_time:
            continue
        
        # If the customer arrives at the same time as the current time, and Fluttershy is already wearing the same type of clothing, serve the customer immediately
        if arrival_time == current_time and clothing_type == current_clothing:
            num_customers_served += 1
            continue
        
        # If the customer arrives at a different time than the current time, and Fluttershy is already wearing a different type of clothing, remove the current clothing and put on the new clothing
        if arrival_time > current_time and clothing_type != current_clothing:
            removing_time = current_time + removing_times[current_clothing - 1]
            putting_on_time = removal_time + dressing_times[clothing_type - 1]
            
            # If the putting on time is later than the arrival time, skip the customer
            if putting_on_time > arrival_time:
                continue
            
            # Update the current time and current clothing
            current_time = putting_on_time
            current_clothing = clothing_type
            
        # Serve the customer
        num_customers_served += 1
    
    return num_customers_served

def main():
    num_customers, num_clothing_types = map(int, input().split())
    dressing_times = list(map(int, input().split()))
    removing_times = list(map(int, input().split()))
    customers = []
    for _ in range(num_customers):
        customer = list(map(int, input().split()))
        customers.append(customer)
    print(get_max_customers(customers, dressing_times, removing_times))

if __name__ == '__main__':
    main()

