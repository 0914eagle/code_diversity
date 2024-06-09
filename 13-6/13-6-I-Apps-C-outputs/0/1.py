
def f1(n, m, t, op):
    # Initialize a dictionary to store the possible values for each grid square
    values = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            values[(i, j)] = set(range(1, n+1))
    
    # Remove the values that are not possible for the given target and operation
    for i in range(1, n+1):
        for j in range(1, n+1):
            if op == '-':
                values[(i, j)].discard(t - (i + j))
            elif op == '*':
                for k in range(1, n+1):
                    values[(i, j)].discard(t // k)
            elif op == '/':
                for k in range(1, n+1):
                    values[(i, j)].discard(t * k)
    
    # Initialize a list to store the possible assignments of values to grid squares
    assignments = []
    
    # Recursively find all possible assignments of values to grid squares
    def recurse(row, col, assignment):
        if row == n and col == n:
            assignments.append(assignment)
            return
        
        for value in values[(row, col)]:
            assignment[row][col] = value
            if col == n:
                recurse(row+1, 1, assignment)
            else:
                recurse(row, col+1, assignment)
    
    recurse(1, 1, [[0] * n for _ in range(n)])
    
    # Return the number of possible assignments
    return len(assignments)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    t = int(input())
    op = input()
    print(f1(n, m, t, op))

