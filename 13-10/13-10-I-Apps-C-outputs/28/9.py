
def get_optimal_strategy(n, d, b, a):
    # Initialize the optimal strategy as an array of size n
    optimal_strategy = [0] * n
    
    # Initialize the number of hidden students as 0
    hidden_students = 0
    
    # Iterate over each room
    for i in range(n):
        # If the current room has more than b students, write down the room number
        if a[i] > b:
            optimal_strategy[i] = i
        
        # If the current room has less than or equal to b students, hide the students
        else:
            hidden_students += a[i]
    
    # Return the optimal strategy and the number of hidden students
    return optimal_strategy, hidden_students

def get_maximum_x_i(n, d, b, a):
    # Get the optimal strategy and the number of hidden students
    optimal_strategy, hidden_students = get_optimal_strategy(n, d, b, a)
    
    # Initialize the maximum of x_i as 0
    maximum_x_i = 0
    
    # Iterate over each room
    for i in range(n):
        # If the current room has a different number of students than b, add 1 to the maximum of x_i
        if optimal_strategy[i] != 0:
            maximum_x_i += 1
    
    # Return the maximum of x_i
    return maximum_x_i

if __name__ == '__main__':
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_x_i(n, d, b, a))

