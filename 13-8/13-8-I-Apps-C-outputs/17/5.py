
def is_valid_specification(specification, n):
    
    # Check if the specification has n rows and n columns
    if len(specification) != n:
        return False
    for row in specification:
        if len(row) != n:
            return False
    
    # Check if each row has at least one bar
    for row in specification:
        if sum(row) == 0:
            return False
    
    # Check if each column has at least one bar
    transposed_specification = list(map(list, zip(*specification)))
    for column in transposed_specification:
        if sum(column) == 0:
            return False
    
    # Check if no two bars in the same row/column are touching
    for i in range(n):
        for j in range(n):
            if specification[i][j] == 1 and specification[i][j+1] == 1:
                return False
            if specification[i][j] == 1 and specification[i+1][j] == 1:
                return False
    
    return True

def solve_bar_code(specification, n):
    
    # Initialize the solution matrix with all 0s
    solution = [[0] * n for _ in range(n)]
    
    # Fill in the solution matrix based on the specification
    for i in range(n):
        for j in range(n):
            if specification[i][j] == 1:
                solution[i][j] = 1
    
    return solution

def main():
    n = int(input())
    specification = []
    for _ in range(n):
        specification.append(list(map(int, input().split())))
    
    if not is_valid_specification(specification, n):
        print("Invalid specification")
        return
    
    solution = solve_bar_code(specification, n)
    for row in solution:
        print("".join(map(str, row)))

if __name__ == '__main__':
    main()

