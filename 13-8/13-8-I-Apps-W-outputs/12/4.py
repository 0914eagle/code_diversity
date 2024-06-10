
def read_notes(a, b):
    # Initialize variables
    n = 0
    m = 0
    p = []
    q = []
    
    # Loop through all possible values of n
    for n in range(1, a + 1):
        # Calculate the total time spent reading notes in the first day
        time_first_day = sum(range(1, n + 1))
        
        # Check if the total time spent in the first day is less than or equal to a
        if time_first_day <= a:
            # Calculate the total time spent reading notes in the second day
            time_second_day = sum(range(n + 1, n + b + 1))
            
            # Check if the total time spent in the second day is less than or equal to b
            if time_second_day <= b:
                # Add the current value of n to the list of possible values of n
                p.append(n)
                
                # Add the current value of m to the list of possible values of m
                q.append(b - time_second_day)
    
    # Find the largest possible value of n and m
    n = max(p)
    m = max(q)
    
    # Return the list of lecture notes to read in the first day
    return n, p[:n]

def read_notes_alt(a, b):
    # Initialize variables
    n = 0
    m = 0
    p = []
    q = []
    
    # Loop through all possible values of n
    for n in range(1, a + 1):
        # Calculate the total time spent reading notes in the first day
        time_first_day = sum(range(1, n + 1))
        
        # Check if the total time spent in the first day is less than or equal to a
        if time_first_day <= a:
            # Calculate the total time spent reading notes in the second day
            time_second_day = sum(range(n + 1, n + b + 1))
            
            # Check if the total time spent in the second day is less than or equal to b
            if time_second_day <= b:
                # Add the current value of n to the list of possible values of n
                p.append(n)
                
                # Add the current value of m to the list of possible values of m
                q.append(b - time_second_day)
    
    # Find the largest possible value of n and m
    n = max(p)
    m = max(q)
    
    # Return the list of lecture notes to read in the first day
    return n, p[:n]

if __name__ == '__main__':
    a, b = map(int, input().split())
    n, p = read_notes(a, b)
    print(n)
    print(*p)
    print(b - sum(p))
    print(*p)

