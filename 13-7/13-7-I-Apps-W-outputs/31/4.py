
def get_distinct_ball_orders(n, max_throws):
    # Initialize a list to store the number of distinct ball orders
    distinct_ball_orders = 1
    
    # Iterate over the maximum number of throws
    for i in range(max_throws):
        # Calculate the number of distinct ball orders after the current throw
        distinct_ball_orders *= n - 1
        
        # Calculate the number of repeated ball orders after the current throw
        repeated_ball_orders = n * (n - 1) / 2
        
        # Subtract the number of repeated ball orders from the total number of distinct ball orders
        distinct_ball_orders -= repeated_ball_orders
        
        # Modulo the result by 1000000007 to avoid overflow
        distinct_ball_orders %= 1000000007
    
    # Return the number of distinct ball orders
    return distinct_ball_orders

def main():
    # Read the number of students and maximum number of throws from input
    n, max_throws = map(int, input().split())
    
    # Calculate the number of distinct ball orders
    distinct_ball_orders = get_distinct_ball_orders(n, max_throws)
    
    # Print the result
    print(distinct_ball_orders)

if __name__ == '__main__':
    main()

