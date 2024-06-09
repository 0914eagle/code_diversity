
def f1(n, m, t, op):
    # Initialize a dictionary to store the valid assignments for each row and column
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    
    # Initialize a set to store the used numbers
    used = set()
    
    # Iterate over the grid locations
    for _ in range(m):
        r, c = map(int, input().split())
        
        # Check if the current location is valid
        if r < 1 or r > n or c < 1 or c > n:
            return 0
        
        # Check if the current location is already used
        if r in rows and c in cols:
            return 0
        
        # Add the current location to the dictionary
        rows[r - 1].add(c)
        cols[c - 1].add(r)
        
        # Add the current location to the used set
        used.add(r)
        used.add(c)
    
    # Check if all rows and columns have at least one element
    if len(rows) != n or len(cols) != n:
        return 0
    
    # Check if all rows and columns have at most one element
    if len(set(rows)) != 1 or len(set(cols)) != 1:
        return 0
    
    # Check if the target value is valid
    if t not in rows[0] or t not in cols[0]:
        return 0
    
    # Check if all numbers are used
    if len(used) != n:
        return 0
    
    # Check if the operator is valid
    if op not in ['+', '-', '*', '/']:
        return 0
    
    # If all conditions are met, return 1
    return 1

def f2(n, m, t, op):
    # Initialize a dictionary to store the valid assignments for each row and column
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    
    # Initialize a set to store the used numbers
    used = set()
    
    # Iterate over the grid locations
    for _ in range(m):
        r, c = map(int, input().split())
        
        # Check if the current location is valid
        if r < 1 or r > n or c < 1 or c > n:
            return 0
        
        # Check if the current location is already used
        if r in rows and c in cols:
            return 0
        
        # Add the current location to the dictionary
        rows[r - 1].add(c)
        cols[c - 1].add(r)
        
        # Add the current location to the used set
        used.add(r)
        used.add(c)
    
    # Check if all rows and columns have at least one element
    if len(rows) != n or len(cols) != n:
        return 0
    
    # Check if all rows and columns have at most one element
    if len(set(rows)) != 1 or len(set(cols)) != 1:
        return 0
    
    # Check if the target value is valid
    if t not in rows[0] or t not in cols[0]:
        return 0
    
    # Check if all numbers are used
    if len(used) != n:
        return 0
    
    # Check if the operator is valid
    if op not in ['+', '-', '*', '/']:
        return 0
    
    # If all conditions are met, return 1
    return 1

if __name__ == '__main__':
    n, m, t, op = map(int, input().split())
    print(f1(n, m, t, op))
    print(f2(n, m, t, op))

