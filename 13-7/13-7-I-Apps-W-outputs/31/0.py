
def get_ball_order_count(n, throws):
    # Initialize a list to store the number of ball orders for each student
    ball_orders = [0] * n
    # Set the initial ball order as (1, 2, 3, ..., n)
    ball_order = list(range(1, n + 1))
    # Iterate through the throws
    for throw in throws:
        # Get the indices of the students who are participating in the throw
        student_indices = throw - 1
        # Swap the balls of the two students
        ball_order[student_indices[0]], ball_order[student_indices[1]] = ball_order[student_indices[1]], ball_order[student_indices[0]]
    # Return the number of distinct ball orders
    return len(set(ball_order))

def main():
    n = int(input())
    throws = [int(i) for i in input().split()]
    print(get_ball_order_count(n, throws) % 1000000007)

if __name__ == '__main__':
    main()

