
def get_distinct_ball_orders(n, throws):
    # Initialize a list to store the number of distinct ball orders
    distinct_orders = 1
    
    # Iterate over the throws
    for throw in throws:
        # Get the number of balls that will be thrown in this throw
        num_balls = throw[0]
        
        # Get the number of students that will participate in this throw
        num_students = throw[1]
        
        # Calculate the number of distinct ball orders after this throw
        distinct_orders *= num_balls ** num_students
    
    # Return the number of distinct ball orders
    return distinct_orders % 1000000007

def main():
    # Read the number of students and the maximum number of throws from the input
    n, throws = read_input()
    
    # Call the function to get the number of distinct ball orders
    distinct_orders = get_distinct_ball_orders(n, throws)
    
    # Print the result
    print(distinct_orders)

def read_input():
    # Read the number of students and the maximum number of throws from the input
    n = int(input())
    throws = []
    for _ in range(n):
        throws.append(list(map(int, input().split())))
    
    # Return the number of students and the maximum number of throws
    return n, throws

if __name__ == '__main__':
    main()

