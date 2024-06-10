
def solve_query(x1, y1, x2, y2, n, m, c_l, c_e, v):
    # Base case: if x1 == x2 and y1 == y2, return 0
    if x1 == x2 and y1 == y2:
        return 0
    
    # Initialize the minimum time needed to reach (x2, y2) from (x1, y1)
    min_time = float('inf')
    
    # If x1 == x2, we can only move along the same floor
    if x1 == x2:
        # If y1 == y2, we don't need to move at all
        if y1 == y2:
            return 0
        # Otherwise, we need to move through the corridor
        else:
            min_time = abs(y2 - y1)
    
    # If x1 != x2, we can use stairs or elevators to move between floors
    else:
        # Calculate the time needed to move to the nearest floor with a stair or elevator
        if x1 < x2:
            time_to_nearest_stair_or_elevator = min(abs(x2 - x1), abs(x2 - n) - abs(x1 - x2))
        else:
            time_to_nearest_stair_or_elevator = min(abs(x1 - x2), abs(x1 - n) - abs(x2 - x1))
        
        # Calculate the time needed to move between floors using the elevator
        time_to_move_via_elevator = abs(x2 - x1) * v
        
        # Calculate the time needed to move between floors using the stairs
        time_to_move_via_stairs = abs(y2 - y1)
        
        # Calculate the minimum time needed to move between floors
        min_time = min(time_to_nearest_stair_or_elevator + solve_query(x1, y1, x2, y2, n, m, c_l, c_e, v), time_to_move_via_elevator + solve_query(x1, y1, x2, y2, n, m, c_l, c_e, v), time_to_move_via_stairs + solve_query(x1, y1, x2, y2, n, m, c_l, c_e, v))
    
    return min_time

def solve(n, m, c_l, c_e, v, queries):
    # Initialize the answers for the queries
    answers = []
    
    # Iterate over the queries
    for query in queries:
        # Extract the coordinates of the starting and finishing sections for the query
        x1, y1, x2, y2 = query
        
        # Calculate the minimum time needed to reach the destination
        min_time = solve_query(x1, y1, x2, y2, n, m, c_l, c_e, v)
        
        # Add the answer to the list of answers
        answers.append(min_time)
    
    return answers

if __name__ == '__main__':
    # Read the input data
    n, m, c_l, c_e, v = map(int, input().split())
    l = list(map(int, input().split()))
    e = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    # Solve the queries
    answers = solve(n, m, c_l, c_e, v, queries)
    
    # Print the answers
    for answer in answers:
        print(answer)

