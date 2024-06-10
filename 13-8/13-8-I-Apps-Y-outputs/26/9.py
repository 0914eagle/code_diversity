
def get_earliest_delivery_time(A, B, C, D, E):
    # Calculate the delivery times for each dish
    delivery_times = [A, B, C, D, E]
    
    # Find the earliest delivery time
    earliest_delivery_time = min(delivery_times)
    
    return earliest_delivery_time

def main():
    # Read input from stdin
    A, B, C, D, E = map(int, input().split())
    
    # Call the get_earliest_delivery_time function
    earliest_delivery_time = get_earliest_delivery_time(A, B, C, D, E)
    
    # Print the result
    print(earliest_delivery_time)

if __name__ == '__main__':
    main()

