
def is_solvable(n, k, rows):
    # Initialize a set to store the numbers that have been used
    used_numbers = set()
    
    # Iterate through the given rows
    for row in rows:
        # Add the numbers in the row to the set of used numbers
        used_numbers |= set(row)
    
    # Check if all numbers from 1 to n have been used
    return len(used_numbers) == n

def solve(n, k, rows):
    # Initialize a list to store the solution
    solution = []
    
    # Iterate through the remaining rows
    for i in range(k, n):
        # Initialize a list to store the numbers in the current row
        current_row = []
        
        # Iterate through the numbers from 1 to n
        for j in range(1, n + 1):
            # If the number has not been used, add it to the current row
            if j not in used_numbers:
                current_row.append(j)
        
        # Add the current row to the solution
        solution.append(current_row)
    
    # Return the solution
    return solution

def main():
    # Read the input
    n, k = map(int, input().split())
    rows = [list(map(int, input().split())) for _ in range(k)]
    
    # Check if the problem is solvable
    if is_solvable(n, k, rows):
        # Solve the problem
        solution = solve(n, k, rows)
        
        # Print the solution
        for row in solution:
            print(*row)
    else:
        # Print that there is no solution
        print("no")

if __name__ == '__main__':
    main()

