
def count_distinct_ball_orders(n, max_throws):
    # Initialize the number of distinct ball orders to 1
    num_distinct_orders = 1
    
    # Iterate over each student in the line
    for i in range(n):
        # Calculate the number of throws the current student can participate in
        num_throws = min(max_throws[i], n - i)
        
        # Calculate the number of distinct ball orders for the current student
        num_distinct_orders *= num_throws + 1
        
        # Calculate the number of distinct ball orders for the remaining students
        for j in range(i + 1, n):
            num_distinct_orders *= num_throws + 1
    
    # Return the number of distinct ball orders
    return num_distinct_orders % 1000000007

