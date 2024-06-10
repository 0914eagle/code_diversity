
def get_ball_orders(n, throws):
    # Initialize a list to store the ball orders
    ball_orders = []
    
    # Base case: if there is only one student, return the ball order [1]
    if n == 1:
        return [1]
    
    # Recursive case: for each student, get the ball orders for the remaining students
    for i in range(n):
        # Get the ball orders for the students on the left and right of the current student
        left_ball_orders = get_ball_orders(i, throws)
        right_ball_orders = get_ball_orders(n - i - 1, throws)
        
        # For each ball order for the left students, append the current student's ball order
        for left_ball_order in left_ball_orders:
            # Get the current student's ball order
            current_student_ball_order = (i + 1) * throws
            
            # Append the current student's ball order to the left student's ball order
            ball_orders.append(left_student_ball_order + current_student_ball_order)
        
        # For each ball order for the right students, append the current student's ball order
        for right_ball_order in right_ball_orders:
            # Get the current student's ball order
            current_student_ball_order = (n - i) * throws
            
            # Append the current student's ball order to the right student's ball order
            ball_orders.append(right_student_ball_order + current_student_ball_order)
    
    # Return the list of ball orders
    return ball_orders

def get_number_of_distinct_ball_orders(n, throws):
    # Get the list of ball orders
    ball_orders = get_ball_orders(n, throws)
    
    # Get the number of distinct ball orders
    number_of_distinct_ball_orders = len(set(ball_orders))
    
    # Return the number of distinct ball orders
    return number_of_distinct_ball_orders

if __name__ == '__main__':
    n = int(input())
    throws = list(map(int, input().split()))
    print(get_number_of_distinct_ball_orders(n, throws))

