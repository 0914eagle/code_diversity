
def get_ball_orders(n, throws):
    # Initialize a list to store the ball orders
    ball_orders = []
    
    # Base case: if there is only one student, return the ball order (1)
    if n == 1:
        return [1]
    
    # Recursive case: for each student, try all possible ball orders
    for i in range(1, n+1):
        # Get the ball order for the current student
        current_ball_order = i
        
        # Get the ball order for the remaining students
        remaining_ball_order = get_ball_orders(n-1, throws-1)
        
        # Add the current ball order to the list of ball orders
        ball_orders.extend([current_ball_order+remaining_ball_order for remaining_ball_order in remaining_ball_order])
    
    return ball_orders

def get_distinct_ball_orders(n, throws):
    # Get all possible ball orders
    ball_orders = get_ball_orders(n, throws)
    
    # Return the number of distinct ball orders
    return len(set(ball_orders))

if __name__ == '__main__':
    n = int(input())
    throws = list(map(int, input().split()))
    print(get_distinct_ball_orders(n, throws) % 1000000007)

