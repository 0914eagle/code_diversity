
def get_min_time(x1, y1, x2, y2, n, m, c_l, c_e, v):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # If the sections are on the same floor, return the absolute difference between them
    if x1 == x2:
        return abs(y1 - y2)
    
    # If the sections are on different floors, check if there is an elevator between them
    if x2 - x1 == 1:
        # If there is an elevator between the floors, return the time it takes to use the elevator
        if y1 in e_pos and y2 in e_pos:
            return v
        # If there is no elevator between the floors, return the time it takes to use the stairs
        else:
            return abs(y1 - y2)
    
    # If the sections are not on the same floor and there is no elevator between them, return the minimum time it takes to go from the starting section to the elevator and from the elevator to the destination section
    else:
        # Get the positions of the elevators between the floors
        e_pos_between = []
        for i in range(x1+1, x2):
            e_pos_between += [e for e in e_pos if e > y1 and e < y2]
        
        # If there are no elevators between the floors, return the time it takes to use the stairs
        if not e_pos_between:
            return abs(y1 - y2)
        
        # If there is an elevator between the floors, return the minimum time it takes to use the elevator and the stairs
        else:
            # Get the minimum time it takes to use the elevator and the stairs
            min_time = min(min_time, get_min_time(x1, y1, x1+1, e, n, m, c_l, c_e, v) + get_min_time(x1+1, e, x2, y2, n, m, c_l, c_e, v))
            
            # Return the minimum time
            return min_time

def main():
    # Read the input
    n, m, c_l, c_e, v = map(int, input().split())
    l_pos = list(map(int, input().split()))
    e_pos = list(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    
    # Solve the queries
    for query in queries:
        x1, y1, x2, y2 = query
        print(get_min_time(x1, y1, x2, y2, n, m, c_l, c_e, v))

if __name__ == '__main__':
    main()

