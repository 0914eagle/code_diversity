
def get_ball_orders(n, throws):
    # Initialize a list to store the ball orders
    ball_orders = []
    
    # Base case: if there is only one student, return the ball order [1]
    if n == 1:
        return [1]
    
    # Recursive case: if there are more than one student, find the ball orders for the first student and the remaining students
    for i in range(1, throws[0] + 1):
        # Find the ball orders for the first student
        first_student_orders = get_ball_orders(n - 1, throws[1:])
        
        # Find the ball orders for the remaining students
        remaining_students_orders = get_ball_orders(n - 1, throws[1:])
        
        # Combine the ball orders for the first student and the remaining students
        for order in first_student_orders:
            for remaining_order in remaining_students_orders:
                ball_orders.append(order * 10 + remaining_order)
    
    return ball_orders

def get_distinct_ball_orders(n, throws):
    # Get all the ball orders
    all_ball_orders = get_ball_orders(n, throws)
    
    # Remove duplicates
    distinct_ball_orders = list(set(all_ball_orders))
    
    return len(distinct_ball_orders)

def main():
    n = int(input())
    throws = list(map(int, input().split()))
    print(get_distinct_ball_orders(n, throws))

if __name__ == '__main__':
    main()

